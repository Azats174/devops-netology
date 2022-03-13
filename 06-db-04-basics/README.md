
# Домашнее задание к занятию "Домашнее задание к занятию "6.4. POSTgreSQL""

## Обязательная задача 1

Поднял докер используя  следующий манифест
```
version 3.1
services:
  db:
    image: postgres:13.1
    restart: always
    container_name: test_3
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: 123
      POSTGRES_DB: mydb
    volumes:
#       - ./data:/var/lib/postgresql/data
       - ./backup:/backup
    ports:
      - "5432:5432"
  ```
  
Список баз. Я не удержался востановил с бэкапа в  базу mydb 

```
mydb=# \l
                             List of databases
   Name    | Owner | Encoding |  Collate   |   Ctype    | Access privileges 
-----------+-------+----------+------------+------------+-------------------
 mydb      | test  | UTF8     | en_US.utf8 | en_US.utf8 | 
 postgres  | test  | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | test  | UTF8     | en_US.utf8 | en_US.utf8 | =c/test          +
           |       |          |            |            | test=CTc/test
 template1 | test  | UTF8     | en_US.utf8 | en_US.utf8 | =c/test          +
           |       |          |            |            | test=CTc/test
 test_db   | test  | UTF8     | en_US.utf8 | en_US.utf8 | 

```

Подключения к базе
```
mydb=# \c mydb
You are now connected to database "mydb" as user "postgres".
```
```
mydb=# \dt
         List of relations
 Schema |  Name  | Type  |  Owner
--------+--------+-------+----------
 public | orders | table | postgres
(1 row)
```

Структура  таблицы orders
```
mydb=#  \dS+ orders
                                                       Table "public.orders"
 Column |         Type          | Collation | Nullable |              Default               | Storage  | Stats target
| Description
--------+-----------------------+-----------+----------+------------------------------------+----------+--------------
+-------------
 id     | integer               |           | not null | nextval('orders_id_seq'::regclass) | plain    |
|
 title  | character varying(80) |           | not null |                                    | extended |
|
 price  | integer               |           |          | 0                                  | plain    |
|
Indexes:
    "orders_pkey" PRIMARY KEY, btree (id)
Access method: heap
```
Вышел из базы

mydb=# \q
root@9f7a0c51c610:/

### Обязательная задача 2

Создал базу 
```
postgres=# CREATE DATABASE test_database;
CREATE DATABASE
```
Востановил с бэкапа
root@9f7a0c51c610:/# psql -U postgres -f /backup/pg_backup.sql test_database 

Поодключился к базе
```
postgres=# \c test_database
Password: 
You are now connected to database "test_database" as user "postgres".
test_database=# \dt
         List of relations
 Schema |  Name  | Type  |  Owner   
--------+--------+-------+----------
 public | orders | table | postgres
(1 row)
```
провел операцию ANALYZE для сбора статистики по таблице
```
test_database=# ANALYZE VERBOSE public.orders;
INFO:  analyzing "public.orders"
INFO:  "orders": scanned 1 of 1 pages, containing 8 live rows and 0 dead rows; 8 rows in sample, 8 estimated total rows
ANALYZE
```
нашел столбец таблицы orders с наибольшим средним значением размера элементов в байтах
```
test_database=#  select avg_width from pg_stats where tablename='orders';
 avg_width
-----------
         4
        16
         4
(3 rows)
```
###обязательная задача 3

Нужно преобразовать существующую таблицу в партиционированную поэтому пересоздадим таблицу 

```
test_database=# alter table orders rename to orders_simple;
ALTER TABLE

test_database=# create table orders (id integer, title varchar(80), price integer) partition by range(price);
CREATE TABLE

test_database=# create table orders_less499 partition of orders for values from (0) to (499);
CREATE TABLE

create table orders_more499 partition of orders for values from (499) to (999999999);
CREATE TABLE

test_database=#  insert into orders (id, title, price) select * from orders_simple;
INSERT 0 8



```
При изначальном проектировании таблиц можно было сделать ее секционированной, тогда не пришлось бы переименовывать исходную таблицу и переносить данные в новую


###Обязательная задача 4

Создаем бэкап
```
root@9f7a0c51c610:/#pg_dump -U postgres -d test_database > /backup/test_database_dump.sql
```

Для уникальности можно добавить индекс или первичный ключ.

    CREATE INDEX ON orders ((lower(title)));
