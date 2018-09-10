#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/21 17:58
# Python3.5
# response params entity
# @Author  : cunxi.wang
class ResponseMessage:
    _status = False  # processing request status
    _data = ""  # processing request message

    def __init__(self):
        pass

    def print(self):
        print(self._status, self._data)
