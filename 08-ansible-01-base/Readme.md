## 08-ansible-01-base
1. 
```
ansible-playbook -i inventory/test.yml site.yml

PLAY [Print os facts] ************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
[WARNING]: Platform linux on host localhost is using the discovered Python interpreter at /usr/bin/python, but future
installation of another Python interpreter could change this. See
https://docs.ansible.com/ansible/2.9/reference_appendices/interpreter_discovery.html for more information.
ok: [localhost]

TASK [Print OS] ******************************************************************************************************
ok: [localhost] => {
    "msg": "elementary OS"
}

TASK [Print fact] ****************************************************************************************************
ok: [localhost] => {
    "msg": 12
}

PLAY RECAP ***********************************************************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 

```


2.
```
ansible-playbook -i inventory/test.yml site.yml

PLAY [Print os facts] ************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
[WARNING]: Platform linux on host localhost is using the discovered Python interpreter at /usr/bin/python, but future
installation of another Python interpreter could change this. See
https://docs.ansible.com/ansible/2.9/reference_appendices/interpreter_discovery.html for more information.
ok: [localhost]

TASK [Print OS] ******************************************************************************************************
ok: [localhost] => {
    "msg": "elementary OS"
}

TASK [Print fact] ****************************************************************************************************
ok: [localhost] => {
    "msg": "all default fact"
}

PLAY RECAP ***********************************************************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
3.

```
CONTAINER ID   IMAGE     COMMAND            CREATED          STATUS          PORTS     NAMES
ca169a00c225   centos    "sleep infinity"   52 minutes ago   Up 52 minutes             centos7
6fa4d4a9d741   ubuntu    "sleep infinity"   53 minutes ago   Up 53 minutes             ubuntu
```
4.
```
ansible-playbook -i inventory/prod.yml site.yml

PLAY [Print os facts] ************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
ok: [ubuntu]
ok: [centos7]

TASK [Print OS] ******************************************************************************************************
ok: [centos7] => {
    "msg": "CentOS"
}
ok: [ubuntu] => {
    "msg": "Ubuntu"
}

TASK [Print fact] ****************************************************************************************************
ok: [centos7] => {
    "msg": "el"
}
ok: [ubuntu] => {
    "msg": "deb"
}

PLAY RECAP ***********************************************************************************************************
centos7                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ubuntu                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```

5.

```
 cat group_vars/deb/examp.yml ;echo ""
---
  some_fact: "deb default fact"
```
```
cat group_vars/el/examp.yml ;echo ""
---
  some_fact: "el default fact"
```

6.
```

nsible-playbook -i inventory/prod.yml site.yml 

PLAY [Print os facts] ************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
ok: [ubuntu]
ok: [centos7]

TASK [Print OS] ******************************************************************************************************
ok: [centos7] => {
    "msg": "CentOS"
}
ok: [ubuntu] => {
    "msg": "Ubuntu"
}

TASK [Print fact] ****************************************************************************************************
ok: [centos7] => {
    "msg": "el  default fact"
}
ok: [ubuntu] => {
    "msg": "deb  default fact"
}

PLAY RECAP ***********************************************************************************************************
centos7                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ubuntu                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

```

7.

```
ansible-vault encrypt group_vars/deb/examp.yml 
New Vault password: 
Confirm New Vault password: 
Encryption successful
azat@nout2:~/netology/mnt-homeworks/08-ansible-01-base/playbook$ ansible-vault encrypt group_vars/el/examp.yml
New Vault password: 
Confirm New Vault password: 
Encryption successful
```
8.
```
ansible-playbook -i inventory/prod.yml site.yml --ask-vault-pass
Vault password: 

PLAY [Print os facts] ************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
ok: [ubuntu]
ok: [centos7]

TASK [Print OS] ******************************************************************************************************
ok: [centos7] => {
    "msg": "CentOS"
}
ok: [ubuntu] => {
    "msg": "Ubuntu"
}

TASK [Print fact] ****************************************************************************************************
ok: [centos7] => {
    "msg": "el  default fact"
}
ok: [ubuntu] => {
    "msg": "deb  default fact"
}

PLAY RECAP ***********************************************************************************************************
centos7                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ubuntu                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```
9.

Для control mode нужен local

10.
```
 cat inventory/prod.yml ; echo ""
---
  el:
    hosts:
      centos7:
        ansible_connection: docker
  deb:
    hosts:
      ubuntu:
        ansible_connection: docker
  local:
    hosts:
      localhost:
        ansible_connection: local
```

11.

```
ansible-playbook -i inventory/prod.yml site.yml --ask-vault-pass
Vault password: 

PLAY [Print os facts] ************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
[WARNING]: Platform linux on host localhost is using the discovered Python interpreter at /usr/bin/python, but future
installation of another Python interpreter could change this. See
https://docs.ansible.com/ansible/2.9/reference_appendices/interpreter_discovery.html for more information.
ok: [localhost]
ok: [ubuntu]
ok: [centos7]

TASK [Print OS] ******************************************************************************************************
ok: [localhost] => {
    "msg": "elementary OS"
}
ok: [centos7] => {
    "msg": "CentOS"
}
ok: [ubuntu] => {
    "msg": "Ubuntu"
}

TASK [Print fact] ****************************************************************************************************
ok: [localhost] => {
    "msg": 12
}
ok: [centos7] => {
    "msg": "el  default fact"
}
ok: [ubuntu] => {
    "msg": "deb  default fact"
}

PLAY RECAP ***********************************************************************************************************
centos7                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
localhost                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ubuntu                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  

```

Добавил отдельный group-vars для local
```
 ansible-playbook -i inventory/prod.yml site.yml --ask-vault-pass
Vault password: 

PLAY [Print os facts] ************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
[WARNING]: Platform linux on host localhost is using the discovered Python interpreter at /usr/bin/python, but future
installation of another Python interpreter could change this. See
https://docs.ansible.com/ansible/2.9/reference_appendices/interpreter_discovery.html for more information.
ok: [localhost]
ok: [ubuntu]
ok: [centos7]

TASK [Print OS] ******************************************************************************************************
ok: [localhost] => {
    "msg": "elementary OS"
}
ok: [centos7] => {
    "msg": "CentOS"
}
ok: [ubuntu] => {
    "msg": "Ubuntu"
}

TASK [Print fact] ****************************************************************************************************
ok: [localhost] => {
    "msg": "local default fact"
}
ok: [centos7] => {
    "msg": "el  default fact"
}
ok: [ubuntu] => {
    "msg": "deb  default fact"
}

PLAY RECAP ***********************************************************************************************************
centos7                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
localhost                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ubuntu                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```


