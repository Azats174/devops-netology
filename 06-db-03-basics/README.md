
# Домашнее задание к занятию "Домашнее задание к занятию "6.3. MYSQL""

## Обязательная задача 1

Использую манифест для  поднятия контайнера
```
version: '3.1'
services:
  db:
    image: mysql:8
    restart: always
    ports:
      - 3306:3306
    volumes:
      - ~/mysql:/var/lib/mysql
      - ./backup:/backup

    environment:
      - MYSQL_ROOT_PASSWORD=S3cret
      - MYSQL_PASSWORD=An0thrS3crt
      - MYSQL_USER=test
      - MYSQL_DATABASE=test_db    
```

Востанавливаю с бэкапа
```
mysql -p  test_db < /backup/test_dump.sql
```

Версия сервера
```
mysql> \s
--------------
mysql  Ver 8.0.28 for Linux on x86_64 (MySQL Community Server - GPL)

Connection id:		14
Current database:	
Current user:		root@localhost
SSL:			Not in use
Current pager:		stdout
Using outfile:		''
Using delimiter:	;
Server version:		8.0.28 MySQL Community Server - GPL
Protocol version:	10
Connection:		Localhost via UNIX socket
Server characterset:	utf8mb4
Db     characterset:	utf8mb4
Client characterset:	latin1
Conn.  characterset:	latin1
UNIX socket:		/var/run/mysqld/mysqld.sock
Binary data as:		Hexadecimal
Uptime:			10 min 57 sec

Threads: 2  Questions: 52  Slow queries: 0  Opens: 154  Flush tables: 3  Open tables: 72  Queries per second avg: 0.079
```
переключаюсь на базу test_db
```
mysql> use test_db;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
```
вывожу список таблиц
```
mysql> 
mysql> show tables;
+-------------------+
| Tables_in_test_db |
+-------------------+
| orders            |
+-------------------+
1 row in set (0.00 sec)
```
количество записей с price > 300
```

mysql> 
mysql> select count(*) from orders where price >300;
+----------+
| count(*) |
+----------+
|        1 |
+----------+
1 row in set (0.01 sec)

```

## Обязательная задача 2
``
mysql>  CREATE USER 'test'@'localhost' IDENTIFIED BY 'test-pass';
Query OK, 0 rows affected (0.12 sec)

mysql> ALTER USER 'test'@'localhost' ATTRIBUTE '{"fname":"James", "lname":"Pretty"}';
Query OK, 0 rows affected (0.13 sec)


mysql> ALTER USER 'test'@'localhost' WITH MAX_QUERIES_PER_HOUR 100 
    -> PASSWORD EXPIRE INTERVAL 180 DAY
    -> FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2;
Query OK, 0 rows affected (0.12 sec)

mysql> GRANT Select ON test_db.orders TO 'test'@'localhost';
Query OK, 0 rows affected, 1 warning (0.08 sec)

mysql> SELECT * FROM INFORMATION_SCHEMA.USER_ATTRIBUTES WHERE USER='test';
+------+-----------+---------------------------------------+
| USER | HOST      | ATTRIBUTE                             |
+------+-----------+---------------------------------------+
| test | %         | NULL                                  |
| test | localhost | {"fname": "James", "lname": "Pretty"} |
+------+-----------+---------------------------------------+
2 rows in set (0.00 sec)
``


## Обязательная задача 3

``

mysql> SELECT TABLE_NAME,ENGINE,ROW_FORMAT,TABLE_ROWS,DATA_LENGTH,INDEX_LENGTH FROM information_schema.TABLES WHERE table_name = 'orders' and  TABLE_SCHEMA = 'test_db' ORDER BY ENGINE asc;
+------------+--------+------------+------------+-------------+--------------+
| TABLE_NAME | ENGINE | ROW_FORMAT | TABLE_ROWS | DATA_LENGTH | INDEX_LENGTH |
+------------+--------+------------+------------+-------------+--------------+
| orders     | InnoDB | Dynamic    |          5 |       16384 |            0 |
+------------+--------+------------+------------+-------------+--------------+
1 row in set (0.05 sec)

mysql> 

``

``
mysql> ALTER TABLE orders ENGINE = MyISAM;
Query OK, 5 rows affected (1.20 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> ALTER TABLE orders ENGINE = InnoDB;
Query OK, 5 rows affected (1.40 sec)
Records: 5  Duplicates: 0  Warnings: 0

``

``
mysql> show profiles;
+----------+------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Query_ID | Duration   | Query                                                                                                                                                                                |
+----------+------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|        1 | 0.05459025 | SELECT TABLE_NAME,ENGINE,ROW_FORMAT,TABLE_ROWS,DATA_LENGTH,INDEX_LENGTH FROM information_schema.TABLES WHERE table_name = 'orders' and  TABLE_SCHEMA = 'test_db' ORDER BY ENGINE asc |
|        2 | 1.19558400 | ALTER TABLE orders ENGINE = MyISAM                                                                                                                                                   |
|        3 | 1.40615800 | ALTER TABLE orders ENGINE = InnoDB                                                                                                                                                   |
+----------+------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
3 rows in set, 1 warning (0.00 sec)
``

## Обязательная задача 4


``

[mysqld]
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
datadir         = /var/lib/mysql
secure-file-priv= NULL
#Set IO Speed
innodb_flush_log_at_trx_commit = 0 

#Set compression
innodb_file_format=Barracuda

#Set buffer
innodb_log_buffer_size	= 1M

#Set Cache size
key_buffer_size = 640M

#Set log size
max_binlog_size	= 100M
``
