#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/21 17:55
# Python3.5
# @Author  : cunxi.wang

import socket
import time

from socketlean.entity.AskNews import AskNews
from socketlean.entity.News import News
from socketlean.utils import ConstantUtils


class ServerSocket:
    _ip = ""
    _port = ""
    _max_block_size = 1
    _serversocket = ""
    _runaccept = True
    _clientlist = []

    def __init__(self, ip, port, max_block_size):
        self._ip = ip
        self._port = port
        self._max_block_size = max_block_size

    def startserversocket(self):
        ## 创建socket对象
        self._serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._serversocket.bind((self._ip, self._port))
        ## 设置最大连接数,超过后排队
        self._serversocket.listen(self._max_block_size)
        print("server socket started")
        while self._runaccept:
            print("waiting for client connection")
            _client, _addr = self._serversocket.accept()  # listen client link
            self.receivedata(_client, self.handlerexecutereceivedata)
            print(_client, " client is connected")
            self._clientlist.append(_client)

    def receivedata(self, client, handlerexecutereceivedata):
        _data = client.recv(ConstantUtils.BUFFER_SIZE)
        print("receive data:", _data)
        if handlerexecutereceivedata:
            handlerexecutereceivedata(client, _data)

    def handlerexecutereceivedata(self, client, data):   # Receive message callback function
        _news = News(0)
        _news.__dict__ = eval(data.decode(encoding='utf-8'))
        _news.print()
        _asknews=AskNews()

        if _news._newstype == 1:
            _asknews._status = True
            _asknews._message="登录成功"
        elif _news._newstype == 2:
            _asknews._status = True
            _asknews._message="心跳成功"
        else:
            _asknews._message="操作失败"
        self.senddata(client, _asknews)

    def senddata(self, client, data):
        _data = str(data.__dict__)
        print("json obj to string data:", _data)
        client.send(_data.encode("UTF-8"))

    def stopserversocket(self):
        self._runaccept = False
        self._serversocket.close()

# 主入口
def main():
    serverSocket = ServerSocket(ConstantUtils.IP, ConstantUtils.PORT, ConstantUtils.MAX_CONNECT)
    serverSocket.startserversocket()
    time.sleep(600)
    serverSocket.stopserversocket()

if __name__ == '__main__':
    main()
