
### Домашнее задание к занятию "09.03 Jenkins"

```
node("ansible_docker"){
    stage("Git checkout"){
        git credentialsId: 'vmkey', url: 'git@github.com:azats174/example-playbook.git'
    }
    stage("Check ssh key"){
        secret_check=true
    }
    stage("Run playbook"){
        if (secret_check){
            sh 'ansible-galaxy install -r requirements.yml'
            sh 'ansible-playbook -i inventory/prod.yml site.yml'
        }
        else{
            echo 'no more keys'
        }
        
    }
}
```
requirements.yml

```
---
  - src: https://github.com/geerlingguy/ansible-role-java.git
    scm: git
    name: geerlingguy.java

```
site.yml
```
---
  - hosts: any
    tasks:
     - name: installing repo for Java 8 in Ubuntu
       apt_repository: repo='ppa:openjdk-r/ppa'
  - hosts: any
    roles:
      - role: geerlingguy.java
        when: "ansible_os_family == 'Debian'"
        java_packages:
          - openjdk-8-jdk

```
