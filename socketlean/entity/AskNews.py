#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/21 17:58
# Python3.5
# response params entity
# @Author  : cunxi.wang
class AskNews:
    _status=False   # processing request status
    _message=""     # processing request message
    def __init__(self):
        pass
    def print(self):
        print(self._status,self._message)