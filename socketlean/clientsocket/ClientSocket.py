#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/21 17:58
# Python3.5
# @Author  : cunxi.wang

import socket
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

    def senddata(self, data):
        self._socket.send(data.encode("utf-8"))

    def receivedata(self, handlerexecutereceivedata):
        _data = self._socket.recv(ConstantUtils.BUFFER_SIZE)
        print("receive data:", _data)
        if handlerexecutereceivedata:
            handlerexecutereceivedata(_data)

    def handlerexecutereceivedata(self, data):   # Receive message callback function
        pass

    def stopsocket(self):
        self._socket.close()


# 主入口
def main():
    clientsocket = ClientSocket(ConstantUtils.IP, ConstantUtils.PORT);
    clientsocket.startsocket()
    clientsocket.senddata("hello...")
    clientsocket.receivedata(clientsocket.handlerexecutereceivedata)
    clientsocket.stopsocket()


if __name__ == '__main__':
    main()
    '''
    quitNum = raw_input('press Nubmer to exit:')
    while True:
      if quitNum.isdigit():
         break
      quitNum = raw_input('press Nubmer to exit:')
    '''
