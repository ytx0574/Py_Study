# coding:utf-8

import sqlite3
import json

conn = sqlite3.connect('sqlite3.db')
# 数据库操作对象
cursor = conn.cursor()

# cursor.execute('drop table user')
# cursor.execute('create table user (id integer primary key autoincrement , name varchar(20), age int)')
# cursor.execute('create table class (class_name varchar(20), member int)')
cursor.execute('insert into user (name, age) values (\'xxx\', 222)')
# cursor.close()
# commit才会写入数据到数据库
cursor.close()
conn.commit()



#获取每一次获取都是不同的对象, 使用完记得关闭
cursor1 = conn.cursor()
print(cursor == cursor1)
# 数据变更操作必须commit, 否则无法更新到数据库.   虽然这里是结果发生了变化, 但是数据库不会发生更改
cursor1.execute('update user set name = \'adc\' where id = 44')
conn.commit()

result = cursor1.execute('select * from user where id =?', (44,))
alldata = result.fetchall()
print json.dumps(alldata)

cursor1.close()
conn.close()

