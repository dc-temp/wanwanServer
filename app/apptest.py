#coding:utf8

from gfirefly.server.globalobject import netserviceHandle
from gfirefly.netconnect.datapack import DataPackProtoc

@netserviceHandle
def echo_1(_conn,data):
    return data

    


