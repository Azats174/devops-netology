
Задача 1

>azat@nout2:~/netology$ sudo docker push azath174/netology:nginx-1.19
The push refers to repository [docker.io/azath174/netology]
4b23ad72c19c: Layer already exists 
f0f30197ccf9: Layer already exists 
eeb14ff930d4: Layer already exists 
c9732df61184: Layer already exists 
4b8db2d7f35a: Layer already exists 
431f409d4c5a: Layer already exists 
02c055ef67f5: Layer already exists 
nginx-1.19: digest: sha256:65e999e50f0f9c36fc2d4d148e1e34681cbaf84f7ab8b361cbeeec0e3acb4462 size: 1777

>azat@nout2:~/netology$ sudo docker pull azath174/netology:nginx-1.19
nginx-1.19: Pulling from azath174/netology
Digest: sha256:65e999e50f0f9c36fc2d4d148e1e34681cbaf84f7ab8b361cbeeec0e3acb4462
Status: Image is up to date for azath174/netology:nginx-1.19
docker.io/azath174/netology:nginx-1.19
azat@nout2:~/netology$ 


Задача 2

Посмотрите на сценарий ниже и ответьте на вопрос: "Подходит ли в этом сценарии использование Docker контейнеров или лучше подойдет виртуальная машина, физическая машина? Может быть возможны разные варианты?"

Детально опишите и обоснуйте свой выбор.

--

Сценарий:

    Высоконагруженное монолитное java веб-приложение;
    Nodejs веб-приложение;
    Мобильное приложение c версиями для Android и iOS;
    Шина данных на базе Apache Kafka;
    Elasticsearch кластер для реализации логирования продуктивного веб-приложения - три ноды elasticsearch, два logstash и две ноды kibana;
    Мониторинг-стек на базе Prometheus и Grafana;
    MongoDB, как основное хранилище данных для java-приложения;
    Gitlab сервер для реализации CI/CD процессов и приватный (закрытый) Docker Registry.

Задача 3

    Запустите первый контейнер из образа centos c любым тэгом в фоновом режиме, подключив папку /data из текущей рабочей директории на хостовой машине в /data контейнера;
    Запустите второй контейнер из образа debian в фоновом режиме, подключив папку /data из текущей рабочей директории на хостовой машине в /data контейнера;
    Подключитесь к первому контейнеру с помощью docker exec и создайте текстовый файл любого содержания в /data;
    Добавьте еще один файл в папку /data на хостовой машине;
    Подключитесь во второй контейнер и отобразите листинг и содержание файлов в /data контейнера.
    
    azat@nout2:~/netology$ sudo docker  ps

>CONTAINER ID   IMAGE     COMMAND   CREATED          STATUS          PORTS     NAMES
e37d082992e3   debian    "cupsd"   10 seconds ago   Up 9 seconds              hardcore_hellman
50a9f922e329   centos    "cupsd"   22 seconds ago   Up 21 seconds             romantic_roentgen
>azat@nout2:~/netology$ sudo docker exec  e37d082992e3  ls  /data

>azat@nout2:~/netology$ sudo docker exec  e37d082992e3  touch  /data/1111

>azat@nout2:~/netology$ sudo docker exec  e37d082992e3  ls  /data
1111

>azat@nout2:~/netology$ sudo docker exec  50a9f922e329  ls  /data
1111

>azat@nout2:~/netology$ mkdir data/123

>azat@nout2:~/netology$ touch data/test2


>azat@nout2:~/netology$ sudo docker exec  50a9f922e329  ls  /data  -l
total 4
-rw-r--r-- 1 root root    0 Jan 29 16:25 1111
drwxrwxr-x 2 1000 1000 4096 Jan 29 16:26 123
-rw-rw-r-- 1 1000 1000    0 Jan 29 16:27 test2


Задача 4 (*)

Воспроизвести практическую часть лекции самостоятельно.

Соберите Docker образ с Ansible, загрузите на Docker Hub и пришлите ссылку вместе с остальными ответами к задачам.
