#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/24 17:25
# Python3.5
# request params entity
# _newstype:1-login, 2-heardbase
# @Author  : cunxi.wang

class RequestMessage:
    _message_type = ""
    _data = ""
    def __init__(self,message_type):
        self._message_type=message_type
    def print(self):
        print(self._message_type,self._data)

class LoginData():
    _username=""
    _password=""
    def __init__(self,username,password):
        self._username=username
        self._password=password
    def print(self):
        print(self._username,self._password)