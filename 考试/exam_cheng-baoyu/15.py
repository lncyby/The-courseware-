#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect('localhost','root','1','czy')

cursor = db.cursor()
cursor.execute('drop table if exists newtab')
sql = "create table newtab(id int not null,name char(20) not null,age int not null,score float not null default 0,primary key(id))"
cursor.execute(sql)
sql = 'insert into newtab (id,name,age,score) values (1,"zhangsan",12,81)'
cursor.execute(sql)
sql = 'insert into newtab (id,name,age,score) values (2,"lisi",13,85)'
cursor.execute(sql)
sql = 'insert into newtab (id,name,age,score) values (3,"wangmazi",14,59.5)'
cursor.execute(sql)
cursor.execute('select * from newtab where score <= 60')
data = cursor.fetchone()
print data
db.close()


