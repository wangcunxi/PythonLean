#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/21 17:58
# Python3.5
# @Author  : cunxi.wang

import socket
import threading

from socketlean.entity.AskNews import AskNews
from socketlean.entity.Log import Log
from socketlean.entity.News import News, Login
from socketlean.utils import ConstantUtils


class ClientSocket(threading.Thread):
    _ip = ""
    _port = ""
    _socket = ""
    _username = ""
    _password = ""

    def __init__(self, ip, port, username, password):
        threading.Thread.__init__(self)
        self._ip = ip
        self._port = port
        self._username = username
        self._password = password

    def run(self):
        connect_status = self.connect()
        if connect_status:
            self.servicelogic()

    def connect(self):
        try:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create client socket
            self._socket.connect((self._ip, self._port))
            print("connected to server...")
            return True
        except Exception as e:
            print("disconnect to server...")
            return False

    def servicelogic(self):
        _log = Log()  # 初始化日志文件
        _log.notetime(1)  # 记录开始时间
        self.login(self._username, self._password)
        self.receivedata(self.processserverrequest)
        _log.notetime(2)  # 记录接收到数据时间
        _log.print()
        self.stopsocket()

    def receivedata(self, processserverrequest):
        _data = self._socket.recv(ConstantUtils.BUFFER_SIZE)
        print("receive data:", _data)
        if processserverrequest:
            processserverrequest(_data)

    def processserverrequest(self, data):  # Receive message callback function
        _asknews = AskNews()
        _asknews.__dict__ = eval(data.decode(encoding='utf-8'))
        _asknews.print()
        if _asknews._status:
            pass
        else:
            pass

    def login(self, username, password):
        _login = Login(username, password)
        _news = News(1)
        _news._data = str(_login.__dict__)
        self.senddata(_news)

    def senddata(self, news: News):
        news.print()
        _data = str(news.__dict__)
        print("json obj to string data:", _data)
        self._socket.send(_data.encode("UTF-8"))

    def stopsocket(self):
        self._socket.close()


# 主入口
def main():
    _clientsocket = ClientSocket(ConstantUtils.IP, ConstantUtils.PORT,"username","password");
    _clientsocket.start()

if __name__ == '__main__':
    main()
    '''
    quitNum = raw_input('press Nubmer to exit:')
    while True:
      if quitNum.isdigit():
         break
      quitNum = raw_input('press Nubmer to exit:')
    '''
