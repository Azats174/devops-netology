
Домашнее задание к занятию "08.03 Работа с Roles"

Ответ:


1. Файл создан
2. Роль скачана

azat@nout2:~/netology/devops-netology/08-ansible-02-playbook/old_playbook$ ansible-galaxy install -r requirements.yml --roles-path ./
- extracting java to /home/azat/netology/devops-netology/08-ansible-02-playbook/old_playbook/java
- java (1.0.1) was installed successfully




Тест выполнен:

azat@nout2:~/netology/devops-netology/08-ansible-02-playbook/old_playbook/java $ molecule test
INFO     default scenario test matrix: dependency, lint, cleanup, destroy, syntax, create, prepare, converge, idempotence, side_effect, verify, cleanup, destroy
INFO     Performing prerun...
WARNING  Computed fully qualified role name of java does not follow current galaxy requirements.
Please edit meta/main.yml and assure we can correctly determine full role name:

galaxy_info:
role_name: my_name  # if absent directory name hosting role is used instead
namespace: my_galaxy_namespace  # if absent, author is used instead

Namespace: https://galaxy.ansible.com/docs/contributing/namespaces.html#galaxy-namespace-limitations
Role: https://galaxy.ansible.com/docs/contributing/creating_role.html#role-names

As an alternative, you can add 'role-name' to either skip_list or warn_list.

INFO     Using ../../../../../.cache/roles/java symlink to current repository in order to enable Ansible to find the role using its expected full name.



<skip some data>

TASK [Delete docker network(s)] ****************************************************************************************************************

PLAY RECAP *************************************************************************************************************************************
localhost                  : ok=2    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Pruning extra files from scenario ephemeral directory



3. Сценарии созданы

azat@nout2:~/netology/elastic-role $ molecule init scenario -d docker
INFO     Initializing new scenario default...
INFO     Initialized scenario in /home/azat/netology/elastic-role/molecule/default successfully.


4. Добавлены Ubuntu:latest, centors:7 , тест запущен

lex@upc:~/netology/elastic-role $ molecule test
INFO     default scenario test matrix: dependency, lint, cleanup, destroy, syntax, create, prepare, converge, idempotence, side_effect, verify, cleanup, destroy
INFO     Performing prerun...
WARNING  Computed fully qualified role name of 08_elastic-role does not follow current galaxy requirements.
Please edit meta/main.yml and assure we can correctly determine full role name:


<skip some data>

PLAY [Converge] ********************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************
ok: [ubuntu]
ok: [centos8]
ok: [centos7]


<skip some data>

PLAY RECAP *************************************************************************************************************************************
centos7                    : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
centos8                    : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
ubuntu                     : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0


<skip some data>

PLAY RECAP *************************************************************************************************************************************
localhost                  : ok=2    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Pruning extra files from scenario ephemeral directory





5. создание новой роли kibana_role

azat@nout2:~/netology $molecule init role -d docker kibana-role
INFO     Initializing new role kibana-role...
Using /etc/ansible/ansible.cfg as config file
- Role kibana-role was created successfully
INFO     Initialized role in /home/azat/netology/kibana-role successfully.



Тестирование роли

azat@nout2:~/netology/kibana-role $ molecule test
INFO     default scenario test matrix: dependency, lint, cleanup, destroy, syntax, create, prepare, converge, idempotence, side_effect, verify, cleanup, destroy
INFO     Performing prerun...
WARNING  Computed fully qualified role name of kibana-role does not follow current galaxy requirements.
Please edit meta/main.yml and assure we can correctly determine full role name:


<skip some data>

PLAY [Converge] ********************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************
ok: [centos7]
ok: [centos8]
ok: [ubuntu]

TASK [Include kibana-role] ******************************************************************************************************************

TASK [kibana-role : Upload tar.gz Kibana from remote URL] ***********************************************************************************
changed: [centos8]
changed: [ubuntu]
changed: [centos7]

TASK [kibana-role : Create directrory for Kibana (/opt/kibana/7.12.0)] **********************************************************************
changed: [centos7]
changed: [ubuntu]
changed: [centos8]

TASK [kibana-role : Extract Kibana in the installation directory] ***************************************************************************
changed: [ubuntu]
changed: [centos8]
changed: [centos7]

TASK [kibana-role : Set environment Kibana] *************************************************************************************************
changed: [ubuntu]
changed: [centos7]
changed: [centos8]

PLAY RECAP *************************************************************************************************************************************
centos7                    : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
centos8                    : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
ubuntu                     : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0



<skip some data>


INFO     Idempotence completed successfully.
INFO     Running default > side_effect
WARNING  Skipping, side effect playbook not configured.
INFO     Running default > verify
INFO     Running Ansible Verifier

PLAY [Verify] **********************************************************************************************************************************

TASK [Example assertion] ***********************************************************************************************************************
ok: [centos8] => {
    "changed": false,
    "msg": "All assertions passed"
}
ok: [centos7] => {
    "changed": false,
    "msg": "All assertions passed"
}
ok: [ubuntu] => {
    "changed": false,
    "msg": "All assertions passed"
}

PLAY RECAP *************************************************************************************************************************************
centos7                    : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
centos8                    : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
ubuntu                     : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Verifier completed successfully.
INFO     Running default > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running default > destroy

PLAY [Destroy] *********************************************************************************************************************************

TASK [Destroy molecule instance(s)] ************************************************************************************************************
changed: [localhost] => (item=centos8)
changed: [localhost] => (item=centos7)
changed: [localhost] => (item=ubuntu)

TASK [Wait for instance(s) deletion to complete] ***********************************************************************************************
FAILED - RETRYING: Wait for instance(s) deletion to complete (300 retries left).
FAILED - RETRYING: Wait for instance(s) deletion to complete (299 retries left).
FAILED - RETRYING: Wait for instance(s) deletion to complete (298 retries left).
changed: [localhost] => (item={'started': 1, 'finished': 0, 'ansible_job_id': '914470095185.89836', 'results_file': '/home/alex/.ansible_async/914470095185.89836', 'changed': True, 'failed': False, 'item': {'image': 'docker.io/pycontribs/centos:8', 'name': 'centos8', 'pre_build_image': True}, 'ansible_loop_var': 'item'})
changed: [localhost] => (item={'started': 1, 'finished': 0, 'ansible_job_id': '48492610635.89861', 'results_file': '/home/alex/.ansible_async/48492610635.89861', 'changed': True, 'failed': False, 'item': {'image': 'docker.io/pycontribs/centos:7', 'name': 'centos7', 'pre_build_image': True}, 'ansible_loop_var': 'item'})
changed: [localhost] => (item={'started': 1, 'finished': 0, 'ansible_job_id': '604199252717.89886', 'results_file': '/home/alex/.ansible_async/604199252717.89886', 'changed': True, 'failed': False, 'item': {'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True}, 'ansible_loop_var': 'item'})

TASK [Delete docker network(s)] ****************************************************************************************************************

PLAY RECAP *************************************************************************************************************************************
localhost                  : ok=2    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Pruning extra files from scenario ephemeral directory



6. разнес все в Defaults

7.Выложил репозитории:
https://github.com/Azats174/elastic-role
https://github.com/Azats174/kibana-role

8. Добавил в файл

---
  - src: git@github.com:Azats174/kibana-role
    scm: git
    version: "1.0.1"
    name: kibana-role 
  - src: git@github.com:Azats174/elastic-role.git
    scm: git
    version: "1.0.1"
    name: elastic-role

9. playbook переработан

azat@nout2:~/netology/devops-netology/08-ansible-02-playbook/playbook$ ansible-playbook -i inventory/prod.yml site.yml

PLAY [all] *************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************
ok: [elastic001]
ok: [kibana001]

TASK [java-role : Upload .tar.gz file containing binaries from local storage] ******************************************************************
changed: [elastic001]
changed: [kibana001]

TASK [java-role : Upload .tar.gz file conaining binaries from remote storage] ******************************************************************
skipping: [elastic001]
skipping: [kibana001]

TASK [java-role : Ensure installation dir exists] **********************************************************************************************
changed: [elastic001]
changed: [kibana001]

TASK [java-role : Extract java in the installation directory] **********************************************************************************
changed: [elastic001]
changed: [kibana001]

TASK [java-role : Export environment variables] ************************************************************************************************
changed: [elastic001]
changed: [kibana001]

PLAY [elasticsearch] ***************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************
ok: [elastic001]

TASK [elastic-role : Upload tar.gz Elasticsearch from remote URL] ******************************************************************************
changed: [elastic001]

TASK [elastic-role : Create directrory for Elasticsearch] **************************************************************************************
changed: [elastic001]

TASK [elastic-role : Extract Elasticsearch in the installation directory] **********************************************************************
changed: [elastic001]

TASK [elastic-role : Set environment Elastic] **************************************************************************************************
changed: [elastic001]

PLAY [kibana] **********************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************
ok: [kibana001]

TASK [kibana-role : Upload tar.gz Kibana from remote URL] **************************************************************************************
changed: [kibana001]

TASK [kibana-role : Create directrory for Kibana (/opt/kibana/7.12.0)] *************************************************************************
changed: [kibana001]

TASK [kibana-role : Extract Kibana in the installation directory] ******************************************************************************
changed: [kibana001]

TASK [kibana-role : Set environment Kibana] ****************************************************************************************************
changed: [kibana001]

PLAY RECAP *************************************************************************************************************************************
elastic001                 : ok=10   changed=8    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
kibana001                  : ok=10   changed=8    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   



10. 11. Все ссылки на репозитории
https://github.com/Azat174/elastic-role
https://github.com/Azat174/kibana-role
https://github.com/Azat174/playbook
