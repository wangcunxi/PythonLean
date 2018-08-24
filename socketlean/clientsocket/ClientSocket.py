#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/21 17:58
# Python3.5
# @Author  : cunxi.wang

import socket
import time

from socketlean.entity.AskNews import AskNews
from socketlean.entity.News import News, Login, HeartBeat
from socketlean.utils import ConstantUtils


class ClientSocket:
    _ip = ""
    _port = ""
    _socket = ""

    def __init__(self, ip, port):
        self._ip = ip
        self._port = port

    def startsocket(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create client socket
        self._socket.connect((self._ip, self._port))

    def senddata(self, news: News):
        news.print()
        _data = str(news.__dict__)
        print("json obj to string data:", _data)
        self._socket.send(_data.encode("UTF-8"))

    def receivedata(self, handlerexecutereceivedata):
        _data = self._socket.recv(ConstantUtils.BUFFER_SIZE)
        print("receive data:", _data)
        if handlerexecutereceivedata:
            handlerexecutereceivedata(_data)

    def handlerexecutereceivedata(self, data):  # Receive message callback function
        _asknews = AskNews()
        _asknews.__dict__ = eval(data.decode(encoding='utf-8'))
        _asknews.print()
        if _asknews._status:
            pass
        else:
            pass

    def login(self,username,password):
        _login = Login(username,password)
        _news = News(1)
        _news._data = str(_login.__dict__)
        self.senddata(_news)

    def heartbeat(self):
        _heartbeat = HeartBeat()
        _news = News(2)
        _news._data = str(_heartbeat.__dict__)
        self.senddata(_news)

    def stopsocket(self):
        self._socket.close()

# 主入口
def main():
    _clientsocket = ClientSocket(ConstantUtils.IP, ConstantUtils.PORT);
    _clientsocket.startsocket()
    _clientsocket.login('wangcunxi', '123456w')
    # _clientsocket.heartbeat()
    _clientsocket.receivedata(_clientsocket.handlerexecutereceivedata)
    _clientsocket.stopsocket()

if __name__ == '__main__':
    main()
    '''
    quitNum = raw_input('press Nubmer to exit:')
    while True:
      if quitNum.isdigit():
         break
      quitNum = raw_input('press Nubmer to exit:')
    '''
