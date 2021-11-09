#-*- codeing = utf-8 -*-
#@Time : 2021/8/23  9:56
#@Author : mch
#@File : test_sq.py
#@Software : PyCharm


import sqlite3

#连接数据库
a = sqlite3.connect("test_1.db")              #打开或创建数据库文件


#创建数据表
# c = a.cursor()                              #获取游标
#
# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         address char(50),
#         salary real);
# '''
# c.execute(sql)                              #执行SQL语句
# a.commit()                                  #提交数据库操作
# a.close()                                   #关闭数据库连接
#
# print("建表成功")


#插入数据

# c = a.cursor()                              #获取游标
#
# sql_1 = '''
#     insert into company (id,name,address,salary)
#     values (1,"qwe","123",6000);
# '''
#
# sql_2 = '''
#     insert into company (id,name,address,salary)
#     values (2,"ryt","456",5000);
# '''
#
# c.execute(sql_1)                              #执行SQL语句
# c.execute(sql_2)
# a.commit()                                  #提交数据库操作
# a.close()                                   #关闭数据库连接
#
# print("插入数据成功")

#查询数据

c = a.cursor()                              #获取游标

sql = "select id ,name,address,salary from company"

b = c.execute(sql)                              #执行SQL语句
for i in b:
    print("id = ",i[0])
    print("name = ",i[1])
    print("address = ",i[2])
    print("salary = ",i[3])
a.close()                                   #关闭数据库连接

print("查询成功")





