
# Домашнее задание к занятию "Домашнее задание к занятию "6.2. SQL""

## Обязательная задача 1

version: '3.1'
services:
  db:
    image: postgres:12.10
    restart: always
    environment:
      POSTGRES_USER: test
      POSTGRES_PASSWORD: test123
      POSTGRES_DB: mydb
    volumes:
       - ./data:/var/lib/postgresql/data
       - ./backup:/backup
    ports:
      - "5432:5432"

## Обязательная задача 2

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



mydb=# \du
                                       List of roles
    Role name     |                         Attributes                         | Member of 
------------------+------------------------------------------------------------+-----------
 test             | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 test-admin-user  | Superuser, No inheritance                                  | {}
 test-simple-user | No inheritance                                             | {}

tast_db=# \dt
        List of relations
 Schema |  Name   | Type  | Owner 
--------+---------+-------+-------
 public | clients | table | test
 public | orders  | table | test
(2 rows)

mydb=# select * from information_schema.table_privileges where grantee in ('test-admin-user','test-simple-user');
 grantor |     grantee      | table_catalog | table_schema | table_name | privilege_type | is_grantable | with_hierarc
hy 
---------+------------------+---------------+--------------+------------+----------------+--------------+-------------
---
 test    | test-simple-user | mydb          | public       | clients    | INSERT         | NO           | NO
 test    | test-simple-user | mydb          | public       | clients    | SELECT         | NO           | YES
 test    | test-simple-user | mydb          | public       | clients    | UPDATE         | NO           | NO
 test    | test-simple-user | mydb          | public       | clients    | DELETE         | NO           | NO
 test    | test-simple-user | mydb          | public       | orders     | INSERT         | NO           | NO
 test    | test-simple-user | mydb          | public       | orders     | SELECT         | NO           | YES
 test    | test-simple-user | mydb          | public       | orders     | UPDATE         | NO           | NO
 test    | test-simple-user | mydb          | public       | orders     | DELETE         | NO           | NO
(8 rows)


test_db=#  
 
SELECT  *  FROM orders;
 id | name | price 
----+------+-------
(0 rows)


test_db=#   
SELECT  *  FROM clients;
 id | lastname | country | booking 
----+----------+---------+---------


test_db=# \d  orders;
               Table "public.orders"
 Column |  Type   | Collation | Nullable | Default 
--------+---------+-----------+----------+---------
 id     | integer |           | not null | 
 name   | text    |           |          | 
 price  | integer |           |          | 
Indexes:
    "orders_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "clients" CONSTRAINT "clients_booking_fkey" FOREIGN KEY (booking) REFERENCES orders(id)


test_db=# \d  clients;
               Table "public.clients"
  Column  |  Type   | Collation | Nullable | Default 
----------+---------+-----------+----------+---------
 id       | integer |           | not null | 
 lastname | text    |           |          | 
 country  | text    |           |          | 
 booking  | integer |           |          | 
Indexes:
    "clients_pkey" PRIMARY KEY, btree (id)
Foreign-key constraints:
    "clients_booking_fkey" FOREIGN KEY (booking) REFERENCES orders(id)



## Обязательная задача 3

test_db=# insert into orders VALUES (1, 'Шоколад', 10), (2, 'Принтер', 3000), (3, 'Книга', 500), (4, 'Монитор', 7000), (5, 'Гитара', 4000);
INSERT 0 5
test_db=# insert into clients VALUES (1, 'Иванов Иван Иванович', 'USA'), (2, 'Петров Петр Петрович', 'Canada'), (3, 'Иоганн Себастьян Бах', 'Japan'), (4, 'Ронни Джеймс Дио', 'Russia'), (5, 'Ritchie Blackmore', 'Russia');
select count (*) from orders;
INSERT 0 5
 count 
-------
     5
(1 row)

test_db=# select count (*) from orders;
 count 
-------
     5
(1 row)

test_db=# select count (*) from clients;
 count 
-------
     5
(1 row)

## Обязательная задача 4

test_db=# update  clients set booking = 3 where id = 1;
update  clients set booking = 4 where id = 2;
update  clients set booking = 5 where id = 3;
UPDATE 1
UPDATE 1
UPDATE 1
test_db=# select * from clients as c where  exists (select id from orders as o where c.booking = o.id) ;
 id |       lastname       | country | booking 
----+----------------------+---------+---------
  1 | Иванов Иван Иванович | USA     |       3
  2 | Петров Петр Петрович | Canada  |       4
  3 | Иоганн Себастьян Бах | Japan   |       5
(3 rows)

test_db=#  select * from clients where booking is not null;
 id |       lastname       | country | booking 
----+----------------------+---------+---------
  1 | Иванов Иван Иванович | USA     |       3
  2 | Петров Петр Петрович | Canada  |       4
  3 | Иоганн Себастьян Бах | Japan   |       5
(3 rows)



## Обязательная задача 5

test_db=# explain select * from clients as c where exists (select id from orders as o where c.booking = o.id);
                               QUERY PLAN                               
------------------------------------------------------------------------
 Hash Join  (cost=37.00..57.24 rows=810 width=72)
   Hash Cond: (c.booking = o.id)
   ->  Seq Scan on clients c  (cost=0.00..18.10 rows=810 width=72)
   ->  Hash  (cost=22.00..22.00 rows=1200 width=4)
         ->  Seq Scan on orders o  (cost=0.00..22.00 rows=1200 width=4)
(5 rows)

test_db=# explain select * from clients  where  booking is not null;
                        QUERY PLAN                         
-----------------------------------------------------------
 Seq Scan on clients  (cost=0.00..18.10 rows=806 width=72)
   Filter: (booking IS NOT NULL)
(2 rows)

## Обязательная задача 6


root@c327ef3c9de4:/# pg_dump -U test test_db -f /backup/dump_test.sql

ls /backup/dump_test.sql -l
-rw-r--r-- 1 root root 2197 Mar  3 06:54 /backup/dump_test.sql

docker-compose down
Stopping 06-db-02-basics_db_1 ... 
db_1  | 2022-03-03 06:56:12.202 UTC [1] LOG:  received fast shutdown request
db_1  | 2022-03-03 06:56:12.272 UTC [1] LOG:  aborting any active transactions
db_1  | 2022-03-03 06:56:12.274 UTC [1] LOG:  background worker "logical replication launcher" (PID 83) exited with exit code 1
db_1  | 2022-03-03 06:56:12.274 UTC [78] LOG:  shutting down
Stopping 06-db-02-basics_db_1 ... done
06-db-02-basics_db_1 exited with code 0
Removing 06-db-02-basics_db_1 ... done
Removing network 06-db-02-basics_default
[1]+  Завершён        docker-compose up

docker exec -it  test_2  bash
root@61f3e26f332f:/# 
root@61f3e26f332f:/# 
root@61f3e26f332f:/#  psql -U test -d test_db -f /backup/dump_test.sql 


test_db=#  \d
        List of relations
 Schema |  Name   | Type  | Owner 
--------+---------+-------+-------
 public | clients | table | test
 public | orders  | table | test
(2 rows)

test_db=#  \l
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
(5 rows)
