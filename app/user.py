# coding=utf-8
import json
from dbmanager import DBManager
from define import *
import glb
import datetime

def pwLogin(name, pw):
	#链接数据库查询用户资料
    db = DBManager(ZERO_DB_NAME)
    cu = db.cursor()
    sql = "".join(["select * from user where name = '", name, "'"])
    cu.execute(sql)
    data = cu.fetchone()
    cu.close()
    if data == None:
        rt = dict(code=ZERO_USERNAME_ERROR)
        return json.dumps(rt)
    if data[3] != pw:
        rt = dict(code=ZERO_PASSWORD_ERROR)
        return json.dumps(rt)

    #计算token
    token = ""
    if glb.ZeroAccountToken['key'].has_key(name) and  \
                    (datetime.datetime.now() - glb.ZeroAccountToken['time'][name]).days < glb.ZeroAccountTokenTimeout:
        token = glb.ZeroAccountToken['key'][name]
        #更新token时间
        glb.ZeroAccountToken['time'][name] = datetime.datetime.now()
    else:
        while True:
            token = glb.strRandom(32)
            if glb.ZeroAccountToken['token'].has_key(token) == False:
                break
        glb.ZeroAccountToken['key'][name] = token
        glb.ZeroAccountToken['time'][name] = datetime.datetime.now()
        glb.ZeroAccountToken['token'][token] = name

    rt = dict(code=0,name=data[1],nickname=data[2],token=token)
    return json.dumps(rt)
	
def tokenLogin(name, token):
    if glb.ZeroAccountToken['key'].has_key(name) and  (datetime.datetime.now() - glb.ZeroAccountToken['time'][name]).days < glb.ZeroAccountTokenTimeout and glb.ZeroAccountToken['key'][name] == token:
        db = DBManager(ZERO_DB_NAME)
        cu = db.cursor()
        sql = "".join(["select * from user where name = '", name, "'"])
        cu.execute(sql)
        data = cu.fetchone()
        cu.close()
        if data == None:
            rt = dict(code=ZERO_USERNAME_ERROR)
            return json.dumps(rt)
        rt = dict(code=0,name=data[1],nickname=data[2],token=token)
        return json.dumps(rt)
    else:
        rt = dict(code=ZERO_PASSWORD_ERROR)
        return json.dumps(rt)

def login(name, pw, token):
    if pw != '':
        return pwLogin(name,pw)
    elif token !='':
        return tokenLogin(name,token)
    rt = dict(code=ZERO_PASSWORD_ERROR)
    return json.dumps(rt)

def logout(token):
    if glb.ZeroAccountToken['token'].has_key(token):
        name = glb.ZeroAccountToken['token'][token]
        del glb.ZeroAccountToken['key'][name]
        del glb.ZeroAccountToken['time'][name]
        del glb.ZeroAccountToken['token'][token]
    rt = dict(code=0)
    return json.dumps(rt)

def createuser(name, nickname, pw):
    #判断用户是否存在
    db = DBManager(ZERO_DB_NAME)
    cu = db.cursor()
    sql = "".join(["select * from user where name = '", name, "'"])
    cu.execute(sql)
    data = cu.fetchone()
    cu.close()
    if data != None:
        rt = dict(code=ZERO_USERNAME_ERROR)
        return json.dumps(rt)
    sql = "insert into user(name,nickname,password) VALUES(?,?,?)"
    db = DBManager(ZERO_DB_NAME)
    cu = db.cursor()
    cu.executemany(sql, [(name, nickname, pw)])
    cu.close()
    rt = dict(code=0,name=name,nickname=nickname)
    return json.dumps(rt)


