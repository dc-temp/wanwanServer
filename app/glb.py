# coding=utf-8
from random import Random

# json数据((filename,data),(filename,time))
ZeroJsonData = { 'data':{}, 'time':{} }

# 计算字符串长度
def strLen(str):
    try:
        row_l=len(str)
        utf8_l=len(str.encode('utf-8'))
        return (utf8_l-row_l)/2+row_l
    except:
        return None
    return None

#账号的token(name,token)
ZeroAccountToken = {'key':{}, 'time':{}, 'token':{}}
#账号超时时间
ZeroAccountTokenTimeout = 1

#计算随机字符串
def strRandom(length=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    l = len(chars) - 1
    random = Random()
    for i in range(length):
        str+=chars[random.randint(0, l)]
    return str


