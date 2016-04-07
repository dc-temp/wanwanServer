# coding=utf-8
from gfirefly.server.globalobject import webserviceHandle
from flask import request
from define import *
import user
import json
import jsonmanager
from glb import strLen

@webserviceHandle('/test',methods=['GET', 'POST'])
def test():
    '''测试案例
    '''
    if request.method == 'POST':
        return request.files['id']
    else:
        print(request.args)
        return "hello,test."

#用户注册
#用户名，昵称，密码
@webserviceHandle('/userregister',methods=['GET'])
def userregister():
    '''用户注册
    '''
    if request.args.has_key('name') and request.args.has_key('nickname') and request.args.has_key('pw'):
        name = request.args['name']
        if strLen(name) < 6:
            rt = dict(code=ZERO_USERNAMELEN_ERROR)
            return json.dumps(rt)
        nickname = request.args['nickname']
        if strLen(nickname) < 6:
            rt = dict(code=ZERO_USERNICKNAMELEN_ERROR)
            return json.dumps(rt)
        pw = request.args['pw']
        if strLen(pw) < 8:
            rt = dict(code=ZERO_USERNICKNAMELEN_ERROR)
            return json.dumps(rt)
        return user.createuser(name,nickname,pw)
    else:
        rt = dict(code=ZERO_DATA_ERROR)
        return json.dumps(rt)

#用户登录
#用户名，密码，token
#用户名和密码可以正常登陆或者用户名和正确的token也可以登陆
@webserviceHandle('/userlogin',methods=['GET'])
def userlogin():
    '''用户登陆
    '''
    if request.args.has_key('name'):
        name = request.args['name']
        pw = ''
        token = ''
        if request.args.has_key('pw'):
            pw = request.args['pw']
        if request.args.has_key('token'):
            token = request.args['token']
        return user.login(name,pw,token)
    else:
        rt = dict(code=ZERO_DATA_ERROR)
        return json.dumps(rt)

#获取表格数据
@webserviceHandle('/table',methods=['GET'])
def table():
    '''获取表格数据
    '''
    if request.args.has_key('name'):
        name = request.args['name']
        return jsonmanager.loadJsonFile(name)
    else:
        rt = dict(code=ZERO_FILENAME_ERROR)
        return json.dumps(rt)


