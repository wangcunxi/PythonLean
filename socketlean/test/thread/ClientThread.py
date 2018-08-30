#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/30 9:14
# Function
# @Author  : cunxi.wang


from socketlean.clientsocket.ClientSocket import ClientSocket
from socketlean.entity.AskNews import AskNews
from socketlean.entity.Log import Log
import threading

class ClientThread(threading.Thread):
    _username = ''
    _password = ''
    _ip=''
    _port=''
    def __init__(self, username, password,ip,port):
        threading.Thread.__init__(self)
        self._username = username
        self._password = password
        self._ip = ip
        self._port = port
    def run(self):
        self.createclient()
    def handlerexecutereceivedata(self, data):  # Receive message callback function
        _asknews = AskNews()
        _asknews.__dict__ = eval(data.decode(encoding='utf-8'))
        _asknews.print()
        if _asknews._status:
            pass
        else:
            pass
    def createclient(self):
        _clientsocket = ClientSocket(self._ip,self._port);
        _clientsocket.startsocket()
        _log = Log()        #初始化日志文件
        _log.notetime(1)    #记录开始时间
        _clientsocket.login(self._username, self._password)
        # _clientsocket.heartbeat()
        _clientsocket.receivedata(self.handlerexecutereceivedata)
        _log.notetime(2)    #记录接收到数据时间
        _log.print()
        _clientsocket.stopsocket()
