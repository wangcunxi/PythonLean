
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/30 9:22
# Function
# @Author  : cunxi.wang
import threading

from socketlean.utils import ConstantUtils

class ReceiveThread(threading.Thread):
    _client = ''
    _handlerexecutereceivedata = ''
    def __init__(self, client, handlerexecutereceivedata):
        threading.Thread.__init__(self)
        self._client = client
        self._handlerexecutereceivedata = handlerexecutereceivedata
    def run(self):
        self.receivedata()
    def receivedata(self):
        _data = self._client.recv(ConstantUtils.BUFFER_SIZE)
        print("receive data:", _data)
        if self._handlerexecutereceivedata:
            self._handlerexecutereceivedata(self._client, _data)


