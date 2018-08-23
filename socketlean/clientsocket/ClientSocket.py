#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/21 17:58
# Python3.5
# @Author  : cunxi.wang

import time
import socket
from pip._vendor.distlib.compat import raw_input
from socketlean.entity import Client
from socketlean.communication import CommunicationThread
from socketlean.utils import ConstantUtils

clientArray = []

def sendmessage(_Socket):
    for i in range(1, 5):
        _Socket.send("hello...".encode("utf-8"))
        time.sleep(1)

def handlerexecutereceivemessage(data, socket):  # receive message callback
    pass

def createclient(ip, port, buffersize):
    client = Client.ClientEntity()
    client.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create client socket
    client.socket.connect((ip, port))
    try:
        client.recvthread = CommunicationThread.RecvMsgThread(client.socket, buffersize,
                                                              handlerexecutereceivemessage)  # create receiver message thread
        client.recvthread.start()
    except:
        print("start receiver message thread fail")
    clientArray.append(client)

# 主入口
def main():
    inputstr = raw_input('please input number:')
    while True:
        if inputstr.isdigit():
            break
            inputstr = raw_input('please input number:')
    createclientcount = int(inputstr)
    # 初始化创建客户端
    while createclientcount > 0:
        createclient(ConstantUtils.IP, ConstantUtils.PORT, ConstantUtils.BUFFER_SIZE)
        createclientcount -= 1
        time.sleep(1)
    for client in clientArray:
        sendmessage(client.socket)
        client.recvthread.stop()
        client.socket.close()

if __name__ == '__main__':
    main()
    '''
    quitNum = raw_input('press Nubmer to exit:')
    while True:
      if quitNum.isdigit():
         break
      quitNum = raw_input('press Nubmer to exit:')
    '''
