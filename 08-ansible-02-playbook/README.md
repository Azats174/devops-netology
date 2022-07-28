# Домашнее задание к занятию "08.02 Работа с Playbook"

## Подготовка к выполнению
1. Сделано
2. Скачайте [playbook](./playbook/) из репозитория с домашним заданием и перенесите его в свой репозиторий.
Сделано
3. Подготовьте хосты в соотвтествии с группами из предподготовленного playbook. 
Создал 2  контейнера
CONTAINER ID   IMAGE           COMMAND     CREATED             STATUS             PORTS     NAMES
201a0f38f7aa   debian:latest   "/bin/sh"   About an hour ago   Up About an hour             elastic001
29eb2b1c1162   debian:latest   "/bin/sh"   2 hours ago         Up 2 hours                   kibana001

4. Скачайте дистрибутив [java](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html) и положите его в директорию `playbook/files/`. 
Сделано

## Основная часть
1. Приготовьте свой собственный inventory файл `prod.yml`.
---
elasticsearch:
   hosts:
    elastic001:
     ansible_connection: docker
kibana:
   hosts:
    kibana001:
      ansible_connection: docker

2. Допишите playbook: нужно сделать ещё один play, который устанавливает и настраивает kibana.
Сделано
3. При создании tasks рекомендую использовать модули: `get_url`, `template`, `unarchive`, `file`.
Сделано
4. Tasks должны: скачать нужной версии дистрибутив, выполнить распаковку в выбранную директорию, сгенерировать конфигурацию с параметрами.
Сделано 
5. Запустите `ansible-lint site.yml` и исправьте ошибки, если они есть.
[201] Trailing whitespace
site.yml:8
            

[201] Trailing whitespace
site.yml:11
    

[403] Package installs should not use latest
site.yml:12
Task/Handler: Install packets

[206] Variables should have spaces before and after: {{ var_name }}
site.yml:13
      apt: name="{{list}}"

[201] Trailing whitespace
site.yml:15
       state=latest 

[201] Trailing whitespace
site.yml:84
   

[201] Trailing whitespace
site.yml:123


6. Попробуйте запустить playbook на этом окружении с флагом `--check`.

ansible-playbook -i inventory/prod.yml site.yml --check

PLAY [Install Java] **************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
[WARNING]: Platform linux on host elastic001 is using the discovered Python interpreter at /usr/bin/python, but
future installation of another Python interpreter could change this. See
https://docs.ansible.com/ansible/2.9/reference_appendices/interpreter_discovery.html for more information.
ok: [elastic001]
[WARNING]: Platform linux on host kibana001 is using the discovered Python interpreter at /usr/bin/python3.7, but
future installation of another Python interpreter could change this. See
https://docs.ansible.com/ansible/2.9/reference_appendices/interpreter_discovery.html for more information.
ok: [kibana001]

TASK [Install packets] ***********************************************************************************************
ok: [kibana001]
ok: [elastic001]

TASK [Set facts for Java 11 vars] ************************************************************************************
ok: [elastic001]
ok: [kibana001]

TASK [Upload .tar.gz file containing binaries from local storage] ****************************************************
ok: [kibana001]
ok: [elastic001]

TASK [Ensure installation dir exists] ********************************************************************************
ok: [elastic001]
ok: [kibana001]

TASK [Extract java in the installation directory] ********************************************************************
skipping: [elastic001]
skipping: [kibana001]

TASK [Export environment variables] **********************************************************************************
ok: [kibana001]
ok: [elastic001]

PLAY [Install Elasticsearch] *****************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
ok: [elastic001]

TASK [Upload tar.gz Elasticsearch from remote URL] *******************************************************************
changed: [elastic001]

TASK [Create directrory for Elasticsearch] ***************************************************************************
ok: [elastic001]

TASK [Extract Elasticsearch in the installation directory] ***********************************************************
skipping: [elastic001]

TASK [Set environment Elastic] ***************************************************************************************
ok: [elastic001]

PLAY [Install Kibana] ************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
ok: [kibana001]

TASK [Upload tar.gz kibana from remote URL] **************************************************************************
ok: [kibana001]

TASK [Create directrory for kibana] **********************************************************************************
ok: [kibana001]

TASK [Extract Kibana in the installation directory] ******************************************************************
skipping: [kibana001]

TASK [Set environment Kibana] ****************************************************************************************
ok: [kibana001]

PLAY RECAP ***********************************************************************************************************
elastic001                 : ok=10   changed=1    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
kibana001                  : ok=10   changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   

azat@nout2:~/netology/devops-netology/08-ansible-02-playbook/playbook$ 

7. Запустите playbook на `prod.yml` окружении с флагом `--diff`. Убедитесь, что изменения на системе произведены.
8. Повторно запустите playbook с флагом `--diff` и убедитесь, что playbook идемпотентен.
 ansible-playbook -i inventory/prod.yml site.yml --diff

PLAY [Install Java] **************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
[WARNING]: Platform linux on host kibana001 is using the discovered Python interpreter at /usr/bin/python3.7, but
future installation of another Python interpreter could change this. See
https://docs.ansible.com/ansible/2.9/reference_appendices/interpreter_discovery.html for more information.
ok: [kibana001]
[WARNING]: Platform linux on host elastic001 is using the discovered Python interpreter at /usr/bin/python, but
future installation of another Python interpreter could change this. See
https://docs.ansible.com/ansible/2.9/reference_appendices/interpreter_discovery.html for more information.
ok: [elastic001]

TASK [Install packets] ***********************************************************************************************
ok: [elastic001]
ok: [kibana001]

TASK [Set facts for Java 11 vars] ************************************************************************************
ok: [elastic001]
ok: [kibana001]

TASK [Upload .tar.gz file containing binaries from local storage] ****************************************************
ok: [kibana001]
ok: [elastic001]

TASK [Ensure installation dir exists] ********************************************************************************
ok: [elastic001]
ok: [kibana001]

TASK [Extract java in the installation directory] ********************************************************************
skipping: [kibana001]
skipping: [elastic001]

TASK [Export environment variables] **********************************************************************************
ok: [kibana001]
ok: [elastic001]

PLAY [Install Elasticsearch] *****************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
ok: [elastic001]

TASK [Upload tar.gz Elasticsearch from remote URL] *******************************************************************
ok: [elastic001]

TASK [Create directrory for Elasticsearch] ***************************************************************************
ok: [elastic001]

TASK [Extract Elasticsearch in the installation directory] ***********************************************************
skipping: [elastic001]

TASK [Set environment Elastic] ***************************************************************************************
ok: [elastic001]

PLAY [Install Kibana] ************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
ok: [kibana001]

TASK [Upload tar.gz kibana from remote URL] **************************************************************************
ok: [kibana001]

TASK [Create directrory for kibana] **********************************************************************************
ok: [kibana001]

TASK [Extract Kibana in the installation directory] ******************************************************************
skipping: [kibana001]

TASK [Set environment Kibana] ****************************************************************************************
ok: [kibana001]

PLAY RECAP ***********************************************************************************************************
elastic001                 : ok=10   changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
kibana001                  : ok=10   changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   

azat@nout2:~/netology/devops-netology/08-ansible-02-playbook/playbook$ 
azat@nout2:~/netology/devops-netology/08-ansible-02-playbook/playbook$ 
azat@nout2:~/netology/devops-netology/08-ansible-02-playbook/playbook$ 
azat@nout2:~/netology/devops-netology/08-ansible-02-playbook/playbook$ 
azat@nout2:~/netology/devops-netology/08-ansible-02-playbook/playbook$ ansible-playbook -i inventory/prod.yml site.yml --check

PLAY [Install Java] **************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
[WARNING]: Platform linux on host elastic001 is using the discovered Python interpreter at /usr/bin/python, but
future installation of another Python interpreter could change this. See
https://docs.ansible.com/ansible/2.9/reference_appendices/interpreter_discovery.html for more information.
ok: [elastic001]
[WARNING]: Platform linux on host kibana001 is using the discovered Python interpreter at /usr/bin/python3.7, but
future installation of another Python interpreter could change this. See
https://docs.ansible.com/ansible/2.9/reference_appendices/interpreter_discovery.html for more information.
ok: [kibana001]

TASK [Install packets] ***********************************************************************************************
ok: [kibana001]
ok: [elastic001]

TASK [Set facts for Java 11 vars] ************************************************************************************
ok: [elastic001]
ok: [kibana001]

TASK [Upload .tar.gz file containing binaries from local storage] ****************************************************
ok: [kibana001]
ok: [elastic001]

TASK [Ensure installation dir exists] ********************************************************************************
ok: [elastic001]
ok: [kibana001]

TASK [Extract java in the installation directory] ********************************************************************
skipping: [elastic001]
skipping: [kibana001]

TASK [Export environment variables] **********************************************************************************
ok: [kibana001]
ok: [elastic001]

PLAY [Install Elasticsearch] *****************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
ok: [elastic001]

TASK [Upload tar.gz Elasticsearch from remote URL] *******************************************************************
changed: [elastic001]

TASK [Create directrory for Elasticsearch] ***************************************************************************
ok: [elastic001]

TASK [Extract Elasticsearch in the installation directory] ***********************************************************
skipping: [elastic001]

TASK [Set environment Elastic] ***************************************************************************************
ok: [elastic001]

PLAY [Install Kibana] ************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
ok: [kibana001]

TASK [Upload tar.gz kibana from remote URL] **************************************************************************
ok: [kibana001]

TASK [Create directrory for kibana] **********************************************************************************
ok: [kibana001]

TASK [Extract Kibana in the installation directory] ******************************************************************
skipping: [kibana001]

TASK [Set environment Kibana] ****************************************************************************************
ok: [kibana001]

PLAY RECAP ***********************************************************************************************************
elastic001                 : ok=10   changed=1    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
kibana001                  : ok=10   changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   

azat@nout2:~/netology/devops-netology/08-ansible-02-playbook/playbook$ 
azat@nout2:~/netology/devops-netology/08-ansible-02-playbook/playbook$ 
azat@nout2:~/netology/devops-netology/08-ansible-02-playbook/playbook$ 
azat@nout2:~/netology/devops-netology/08-ansible-02-playbook/playbook$ ansible-playbook -i inventory/prod.yml site.yml --diff

PLAY [Install Java] **************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
[WARNING]: Platform linux on host kibana001 is using the discovered Python interpreter at /usr/bin/python3.7, but
future installation of another Python interpreter could change this. See
https://docs.ansible.com/ansible/2.9/reference_appendices/interpreter_discovery.html for more information.
ok: [kibana001]
[WARNING]: Platform linux on host elastic001 is using the discovered Python interpreter at /usr/bin/python, but
future installation of another Python interpreter could change this. See
https://docs.ansible.com/ansible/2.9/reference_appendices/interpreter_discovery.html for more information.
ok: [elastic001]

TASK [Install packets] ***********************************************************************************************
ok: [kibana001]
ok: [elastic001]

TASK [Set facts for Java 11 vars] ************************************************************************************
ok: [elastic001]
ok: [kibana001]

TASK [Upload .tar.gz file containing binaries from local storage] ****************************************************
ok: [kibana001]
ok: [elastic001]

TASK [Ensure installation dir exists] ********************************************************************************
ok: [elastic001]
ok: [kibana001]

TASK [Extract java in the installation directory] ********************************************************************
skipping: [elastic001]
skipping: [kibana001]

TASK [Export environment variables] **********************************************************************************
ok: [kibana001]
ok: [elastic001]

PLAY [Install Elasticsearch] *****************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
ok: [elastic001]

TASK [Upload tar.gz Elasticsearch from remote URL] *******************************************************************
ok: [elastic001]

TASK [Create directrory for Elasticsearch] ***************************************************************************
ok: [elastic001]

TASK [Extract Elasticsearch in the installation directory] ***********************************************************
skipping: [elastic001]

TASK [Set environment Elastic] ***************************************************************************************
ok: [elastic001]

PLAY [Install Kibana] ************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
ok: [kibana001]

TASK [Upload tar.gz kibana from remote URL] **************************************************************************
ok: [kibana001]

TASK [Create directrory for kibana] **********************************************************************************
ok: [kibana001]

TASK [Extract Kibana in the installation directory] ******************************************************************
skipping: [kibana001]

TASK [Set environment Kibana] ****************************************************************************************
ok: [kibana001]

PLAY RECAP ***********************************************************************************************************
elastic001                 : ok=10   changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
kibana001                  : ok=10   changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0 

9. Подготовьте README.md файл по своему playbook. В нём должно быть описано: что делает playbook, какие у него есть параметры и теги.


10. Готовый playbook выложите в свой репозиторий, в ответ предоставьте ссылку на него.



---

### Как оформить ДЗ?

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
