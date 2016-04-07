# coding=utf-8
import json
import os
from define import *
import glb

def loadJsonFile(filename):
    # 文件名
    name = "./json/"+filename+".txt"
    # 文件缓存存在并且最后修改时间匹配就返回缓存里的数据
    if glb.ZeroJsonData['data'].has_key(filename) and glb.ZeroJsonData['time'][filename] == os.stat(name):
        rt = "{ \"code\": 0, \"data\": " + glb.ZeroJsonData['data'][filename] + "}"
        return rt

    # 从磁盘读取文件内容
    file = open(name)
    if file == None:
        rt = dict(code=ZERO_FILENAME_ERROR)
        return json.dumps(rt)
    try:
        all_text = file.read()
        glb.ZeroJsonData['data'][filename] = all_text
        glb.ZeroJsonData['time'][filename] = os.stat(name)
    finally:
        file.close( )

    # 返回json数据
    rt = "{ \"code\": 0, \"data\": " + glb.ZeroJsonData['data'][filename] + "}"
    return rt