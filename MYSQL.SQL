password=rakshita_064
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.0.45 MySQL Community Server - GPL

Copyright (c) 2000, 2026, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)

mysql> create database HIT;
Query OK, 1 row affected (0.06 sec)

mysql> show database
    -> show databases;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'database
show databases' at line 1
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| hit                |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)




syntax:
CREATE TABLE table_name (
  column1 datatype constraint,
  column2 datatype constraint,
  column3 datatype constraint,
  ....
);

CREATE TABLE Persons (
  PersonID int PRIMARY KEY,
  LastName varchar(255) NOT NULL,
  FirstName varchar(255),
  Address varchar(255),
  City varchar(255)
);


mysql> create database HIT;
Query OK, 1 row affected (0.06 sec)

mysql> show database
    -> show databases;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'database
show databases' at line 1
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| hit                |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)

mysql> show tables;
ERROR 1046 (3D000): No database selected
mysql> use hit;
Database changed
mysql> show tables;
Empty set (0.07 sec)

mysql> CREATE TABLE Persons (
    ->   PersonID int PRIMARY KEY,
    ->   LastName varchar(255) NOT NULL,
    ->   FirstName varchar(255),
    ->   Address varchar(255),
    ->   City varchar(255)
    -> );
Query OK, 0 rows affected (0.09 sec)

mysql> show tables;
+---------------+
| Tables_in_hit |
+---------------+
| persons       |
+---------------+
1 row in set (0.05 sec)

mysql> desc persons;
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| PersonID  | int          | NO   | PRI | NULL    |       |
| LastName  | varchar(255) | NO   |     | NULL    |       |
| FirstName | varchar(255) | YES  |     | NULL    |       |
| Address   | varchar(255) | YES  |     | NULL    |       |
| City      | varchar(255) | YES  |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+
5 rows in set (0.06 sec)

mysql> insert into persons(PERSONSID,LASTNAME,FIRSTNAME,ADDRESS,CITY)values(101,"Chougule","poorva","shiraguppi","yadur");
ERROR 1054 (42S22): Unknown column 'PERSONSID' in 'field list'
mysql>
mysql>  insert into persons(PersonID,LastName,FirstName,Address,City)values(101,"Chougule","poorva","shiraguppi","yadur");
Query OK, 1 row affected (0.05 sec)

mysql> insert into persons(PersonID,LastName,FirstName,Address,City)values(101,"Chougule","poorva","shiraguppi","yadur");
ERROR 1062 (23000): Duplicate entry '101' for key 'persons.PRIMARY'
mysql> insert into persons(PersonID,LastName,FirstName,Address,City)values(102,"Bedage","Rakshita","shiraguppi","yadur");
Query OK, 1 row affected (0.05 sec)

mysql> select*from persons;
+----------+----------+-----------+------------+-------+
| PersonID | LastName | FirstName | Address    | City  |
+----------+----------+-----------+------------+-------+
|      101 | Chougule | poorva    | shiraguppi | yadur |
|      102 | Bedage   | Rakshita  | shiraguppi | yadur |
+----------+----------+-----------+------------+-------+
2 rows in set (0.00 sec)

mysql> select abs(-44) from dual;
+----------+
| abs(-44) |
+----------+
|       44 |
+----------+
1 row in set (0.03 sec)


mysql> select power (2,4) from dual;
+-------------+
| power (2,4) |
+-------------+
|          16 |
+-------------+
1 row in set (0.02 sec)

mysql> select sqrt(16) from dual;
+----------+
| sqrt(16) |
+----------+
|        4 |
+----------+
1 row in set (0.02 sec)

mysql> select sqrt(64) from dual;
+----------+
| sqrt(64) |
+----------+
|        8 |
+----------+
1 row in set (0.00 sec)

mysql> select exp(4) from dual;
+--------------------+
| exp(4)             |
+--------------------+
| 54.598150033144236 |
+--------------------+
1 row in set (0.00 sec)

mysql> select exp(4) from dual;
+--------------------+
| exp(4)             |
+--------------------+
| 54.598150033144236 |
+--------------------+
1 row in set (0.00 sec)

mysql> select greatest(52,64,18,17,118,35) from dual;
+------------------------------+
| greatest(52,64,18,17,118,35) |
+------------------------------+
|                          118 |
+------------------------------+
1 row in set (0.04 sec)

mysql> select least(3,4,6,8,5,75,64) from dual;
+------------------------+
| least(3,4,6,8,5,75,64) |
+------------------------+
|                      3 |
+------------------------+
1 row in set (0.00 sec)


mysql> select round(4.5) from dual;
+------------+
| round(4.5) |
+------------+
|          5 |
+------------+
1 row in set (0.00 sec)

mysql> select round(4.3) from dual;
+------------+
| round(4.3) |
+------------+
|          4 |
+------------+
1 row in set (0.00 sec)

mysql> select mod(8,3) from dual;
+----------+
| mod(8,3) |
+----------+
|        2 |
+----------+
1 row in set (0.00 sec)

mysql> select lower('HELP4CODE ELEARNING') from dual;
+------------------------------+
| lower('HELP4CODE ELEARNING') |
+------------------------------+
| help4code elearning          |
+------------------------------+
1 row in set (0.04 sec)

mysql> select upper('HELP4CODE ELEARNING') from dual;
+------------------------------+
| upper('HELP4CODE ELEARNING') |
+------------------------------+
| HELP4CODE ELEARNING          |
+------------------------------+
1 row in set (0.03 sec)

mysql> select length('Help4code Elearning') from dual;
+-------------------------------+
| length('Help4code Elearning') |
+-------------------------------+
|                            19 |
+-------------------------------+
1 row in set (0.00 sec)

mysql> select lpad('Help4code','64','_') from dual;
+------------------------------------------------------------------+
| lpad('Help4code','64','_')                                       |
+------------------------------------------------------------------+
| _______________________________________________________Help4code |
+------------------------------------------------------------------+
1 row in set (0.05 sec)


mysql> select REVERSE('HELP4CODE.COM') from dual;
+--------------------------+
| REVERSE('HELP4CODE.COM') |
+--------------------------+
| MOC.EDOC4PLEH            |
+--------------------------+
1 row in set (0.00 sec)

mysql> select ascii('A') from dual;
+------------+
| ascii('A') |
+------------+
|         65 |
+------------+
1 row in set (0.00 sec)

mysql> select ascii('T') from dual;
+------------+
| ascii('T') |
+------------+
|         84 |
+------------+
1 row in set (0.00 sec)

mysql> select 30 + 20 from dual;
+---------+
| 30 + 20 |
+---------+
|      50 |
+---------+
1 row in set (0.03 sec)

mysql> select 30 - 10 from dual;
+---------+
| 30 - 10 |
+---------+
|      20 |
+---------+
1 row in set (0.00 sec)

mysql> select * from persons;
+----------+----------+-----------+------------+-------+
| PersonID | LastName | FirstName | Address    | City  |
+----------+----------+-----------+------------+-------+
|      101 | Chougule | poorva    | shiraguppi | yadur |
|      102 | Bedage   | Rakshita  | shiraguppi | yadur |
+----------+----------+-----------+------------+-------+
2 rows in set (0.00 sec)

