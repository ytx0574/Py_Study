#coding:utf-8

import mysql.connector

conn = mysql.connector.connect(user='root', password='password', database='mysql', use_unicode=True)
cursor = conn.cursor()
cursor.execute('create table Lottery (id integer primary key authorization, lottery_name varchar, open_inteval integer)')

cursor.execute('insert into Lottery (lottery_name, open_interval) values (%s, %s)', ['北京分分彩', 30])
cursor.execute('insert into Lottery (lottery_name, open_interval) values (%s, %s)', ['四川PK⑩', 1])

conn.commit()
cursor.close()
conn.close()


