#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/21 17:58
# Python3.7
# @Author  : cunxi.wang

from datetime import *
import time
import socket
import random
import threading


# socket发送数据线程
from pip._vendor.distlib.compat import raw_input

BUFFER_SIZE = 1024  # 接收数据缓存大小
MAX_CONNECT = 10;   # 最大允许链接数
PORT= 8883          # 设置端口
SEND_MSG_COUNT=2    # 发送数据个数
class sendMsgThread(threading.Thread):
    def __init__(self, threadID, mSocket):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.mSocket = mSocket
    def run(self):
        recvMsg = recvMsgThread(self.threadID, self.mSocket)  # 创建新线程
        recvMsg.start()  # 开启线程
        sendMsgCount = 0;
        while sendMsgCount<SEND_MSG_COUNT:
            try:
                self.mSocket.send(("hello..."+str(sendMsgCount)).encode("utf-8"))
                sendMsgCount+=1
                time.sleep(random.randint(1, 5))
            except Exception as e:
                print( "通讯异常......\n", e)
        recvMsg.stop()
        # close() releases the resource associated with a connection but does not necessarily close the connection immediately. If you want to close the connection in a timely fashion, call shutdown() beforeclose().
        # self.mSocket.shutdown(2)  # 0:SHUT_RD  1:SHUT_WR  2:SHUT_RDWR
        self.mSocket.close()
        print ("关闭客户端发送数据线程____" + str(self.threadID) + "\n")

# socket接收数据线程
class recvMsgThread(threading.Thread):
    def __init__(self, threadID, mSocket):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.mSocket = mSocket
        self.running = True

    def stop(self):
        print( "设置线程是否继续执行标志:" + str(self.running) + "\n")
        self.running = False  # 设置为False

    def run(self):
        print ("启动客户端接收数据线程:" + str(self.threadID) + "\n")
        while self.running:
            try:
                msg = self.mSocket.recv(BUFFER_SIZE)
                print(str(msg))
            except Exception as e:
                print ("客户端异常\n", e)
                break
        print ("关闭客户端接收线程:" + str(self.threadID) + "\n")

def create_Socket(thId):
    # print 'createSocket id:'+str(thId)
    mSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建 socket 对象
    host = socket.gethostname()                                       # 获取本地主机名
    mSocket.connect((host, PORT))
    sendMsg = sendMsgThread(thId, mSocket)  # 创建新线程
    sendMsg.start()  # 开启线程
# 主入口
def main_run():
    inputStr = raw_input('请输入创建客户端的个数:')
    while True:
        if inputStr.isdigit():
            break
        inputStr = raw_input('请输入数字:')
    initSocketCount = int(inputStr)
    index = 1
    # 初始化创建客户端
    while index <= initSocketCount:
        create_Socket(index)
        index += 1
        time.sleep(1)

if __name__ == '__main__':
    main_run()
    '''
    quitNum = raw_input('press Nubmer to exit:')
    while True:
      if quitNum.isdigit():
         break
      quitNum = raw_input('press Nubmer to exit:')
    '''
