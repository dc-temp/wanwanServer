# coding=utf-8
from dbmanager import *
from define import *

def init():
    db = DBManager("../db/main.db")
    cu = db.cursor()

    # 创建表格
    cu.execute("create table if not exists user (id integer primary key,name varchar(320) UNIQUE,nickname text NULL,password varchar(100) NULL,ip varchar(32) NULL)")

    # 添加测试数据
    cu.execute("select * from user where name = 'test@163.com'")
    if cu.fetchone() == None:
        cu.executemany("insert into user(name,nickname,password,ip) VALUES(?,?,?,?)", [('test@163.com', 'test', 'test', '127.0.0.1')])

    cu.close()

init()
