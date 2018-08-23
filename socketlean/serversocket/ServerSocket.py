#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/21 17:55
# Python3.5
# @Author  : cunxi.wang

import socket

from socketlean.entity import Client
from socketlean.communication import CommunicationThread
from socketlean.utils import ConstantUtils

def createserver(ip,port,maxconnect):
    serversocket = socket.socket()     # create socket
    serversocket.bind((ip,port))       # bind ip and port
    serversocket.listen(maxconnect)    # setting links Maximum number client
    print( "server socket started")
    return serversocket;

def handlerexecutereceivemessage(data,socket):       #receive message callback
    data = data.upper()
    socket.send(data.upper())
    print("replye ",socket.getpeername()," data:",data)

def startaccept(serversocket,buffersize):
    while True:
        print( "waiting for client link")
        client = Client.ClientEntity();
        client.socket, client.addr = serversocket.accept()  # listen client link
        try:
            client.recvthread = CommunicationThread.RecvMsgThread(client.socket, buffersize, handlerexecutereceivemessage)  # create recv message thread
            client.recvthread.start()
        except Exception as e:
            print( "start recv message thread fail\n",e)
        print( client," client is connected")

# 主入口
def main():
    serversocket = createserver(ConstantUtils.IP, ConstantUtils.PORT, ConstantUtils.MAX_CONNECT)
    startaccept(serversocket, ConstantUtils.BUFFER_SIZE)

if __name__ == '__main__':
    main()