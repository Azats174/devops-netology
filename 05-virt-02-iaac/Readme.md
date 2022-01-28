#Задача 1

    Опишите своими словами основные преимущества применения на практике IaaC паттернов.
    Какой из принципов IaaC является основополагающим?

*Скорость и уменьшение затрат: IaC позволяет быстрее конфигурировать инфраструктуру и направлен на обеспечение прозрачности, чтобы помочь другим командам со всего предприятия работать быстрее и эффективнее

*Масштабируемость и стандартизация: IaC предоставляет стабильные среды быстро и на должном уровне. Командам разработчиков не нужно прибегать к ручной настройке - они обеспечивают корректность, описывая с помощью кода требуемое состояние сред

*Безопасность и документация: Если за провизионирование всех вычислительных, сетевых и служб хранения отвечает код, они каждый раз будут развертываться одинаково.

*Восстановление в аварийных ситуациях.

С точки зрения отдела разработки первый принцип являеться  главным.
С точки зрения отдела эксплуатации  - 2 и 3
С точки зрения отделя безопасности  - 3
С точки зрения бизнеса  думаю первый   

#Задача 2

    Чем Ansible выгодно отличается от других систем управление конфигурациями?
    Какой, на ваш взгляд, метод работы систем конфигурации более надёжный push или pull?
*

Задача 3

Установить на личный компьютер:

    VirtualBox
    Vagrant
    Ansible

Приложить вывод команд установленных версий каждой из программ, оформленный в markdown.
Задача 4 (*)
azat@azat-MS-16G1:~/.ssh$ VirtualBox --help
Oracle VM VirtualBox Manager 5.2.42_Ubuntu
(C) 2005-2020 Oracle Corporation
All rights reserved.

azat@azat-MS-16G1:~/.ssh$ VirtualBox --help
Oracle VM VirtualBox Manager 5.2.42_Ubuntu
(C) 2005-2020 Oracle Corporation
All rights reserved.
azat@azat-MS-16G1:~/.ssh$  vagrant  version 
Installed Version: 2.0.2

Vagrant was unable to check for the latest version of Vagrant.
Please check manually at https://www.vagrantup.com

azat@azat-MS-16G1:~/.ssh$ ansible  --version 
ansible 2.5.1
  config file = /etc/ansible/ansible.cfg
  configured module search path = [u'/home/azat/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python2.7/dist-packages/ansible
  executable location = /usr/bin/ansible
  python version = 2.7.17 (default, Feb 27 2021, 15:10:58) [GCC 7.5.0]

Воспроизвести практическую часть лекции самостоятельно.

    Создать виртуальную машину.
    Зайти внутрь ВМ, убедиться, что Docker установлен с помощью команды

docker ps
root@vagrant:~# docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES


