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
    "msg": "all default fact"
}

PLAY RECAP ***********************************************************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
