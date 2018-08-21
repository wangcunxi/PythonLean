#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/21 17:55
# Python3.7
# @Author  : cunxi.wang

import socket
import threading

BUFFER_SIZE = 1024  # 接收数据缓存大小
MAX_CONNECT = 10;   # 最大允许链接数
PORT= 8883          # 设置端口
#socket接收数据线程
class recvMsgThread(threading.Thread):
   def __init__(self, socket):
      threading.Thread.__init__(self)
      self.mSocket = socket;
   def run(self):
      print( self.mSocket.getpeername()," 启动接收客户端数据线程")
      while True:
         try:
            msg = self.mSocket.recv(BUFFER_SIZE)
            print( "接收来自",self.mSocket.getpeername()," 的客户端消息:",msg)
            self.mSocket.send(msg.upper())
         except:
            print( "客户端:",self.mSocket.getpeername(),"退出了")
            break
            #threadreading.Thread.exit()
def startServer():
    s = socket.socket()  # 创建 socket 对象
    host = socket.gethostname()  # 获取本地主机名
    s.bind((host, PORT))  # 绑定端口
    s.listen(MAX_CONNECT)  # 设置最大允许连接数
    print( "服务器已启动")
    while True:
        print( "等待客户端链接")
        c, addr = s.accept()  # 建立客户端连接。
        print( addr," 客户端已连接")
        try:
            recvMsg = recvMsgThread(c)  # 创建新的接收线程
            recvMsg.start()
        except:
            print( "启动接收数据线程失败")

if __name__ == '__main__':
    startServer()
