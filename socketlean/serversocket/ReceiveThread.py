# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/30 9:22
# Function
# @Author  : cunxi.wang
import threading

from socketlean.utils import ConstantUtils


class ReceiveThread(threading.Thread):
    _client = ''

    def __init__(self, client, processclientrequest):
        threading.Thread.__init__(self)
        self._client = client
        self.handlerexecutereceivedata = processclientrequest

    def run(self):
        _data = self._client.recv(ConstantUtils.BUFFER_SIZE)
        print("receive data:", _data)
        if self.handlerexecutereceivedata:
            self.handlerexecutereceivedata(self._client, _data)
