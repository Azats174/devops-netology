Задача 1

> ==> yandex: Stopping instance...
==> yandex: Deleting instance...
    yandex: Instance has been deleted!
==> yandex: Creating image: centos-7-base
==> yandex: Waiting for image to complete...
==> yandex: Success image create...
==> yandex: Destroying boot disk...
    yandex: Disk has been deleted!
Build 'yandex' finished after 2 minutes 5 seconds.

> ==> Wait completed after 2 minutes 5 seconds

> ==> Builds finished. The artifacts of successful builds are:
--> yandex: A disk image was created: centos-7-base (id: fd8kpbjuu470k9p9p24n) with family name centos
> azat@nout2:~/netology$ yc compute image list
+----------------------+---------------+--------+----------------------+--------+
|          ID          |     NAME      | FAMILY |     PRODUCT IDS      | STATUS |
+----------------------+---------------+--------+----------------------+--------+
| fd8kpbjuu470k9p9p24n | centos-7-base | centos | f2epin40q8nh7fqdv3sh | READY  |
+----------------------+---------------+--------+----------------------+--------+

Задача 2
![alt text](https://github.com/Azats174/devops-netology/blob/main/05-virt-04-docker-compose/hw_netology_5.4.2.png)

Задача 3

![alt text](https://github.com/Azats174/devops-netology/blob/main/05-virt-04-docker-compose/hw_netology-5.4.3.png)


