#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/23 11:07
# Python3.5
# socket communication class
# 1. RecvMsgThread
# 2. SendMsgThread
# @Author  : cunxi.wang

import threading

class RecvMsgThread(threading.Thread):
    def __init__(self, socket,buffersize,callback):
        threading.Thread.__init__(self)
        self.socket    = socket
        self.buffersize =  buffersize
        self.isRunning  = True
        self.callback   = callback
    def stop(self):
        self.isRunning = False
    def run(self):
        print(self.socket.getpeername()," start reciver message thread")
        while self.isRunning:
            try:
                data = self.socket.recv(self.buffersize)
                print( "receive ",self.socket.getpeername()," data:",data)
                if self.callback:
                    self.callback(data,self.socket)
            except Exception as e:
                print(self.socket, "reciver message thread exit")
                break

class SendMsgThread(threading.Thread):
    def __init__(self, socket,callback):
        threading.Thread.__init__(self)
        self.socket     = socket
        self.isRunning  = True
        self.callback   = callback
    def stop(self):
        self.isRunning = False
    def run(self):
        print(self.socket.getpeername()," start send message thread")
