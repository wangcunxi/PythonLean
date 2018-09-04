#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/21 17:55
# Python3.5
# @Author  : cunxi.wang

import socket
import threading
import time

from socketlean.entity.AskNews import AskNews
from socketlean.entity.News import News
from socketlean.serversocket.ThreadPool import ThreadPool
from socketlean.utils import ConstantUtils


class ServerSocket(threading.Thread):
    _ip = ""
    _port = ""
    _max_block_size = ConstantUtils.MAX_CONNECT
    _replydelaytime = ConstantUtils.DELAYTIME
    _serversocket = ""
    _runaccept = True
    _clients = []
    _threadpool = ""

    def __init__(self, ip, port):
        threading.Thread.__init__(self)
        self._ip    = ip
        self._port  = port
        self._threadpool = ThreadPool()

    def run(self):
        self.listenclient()
        self.accept()

    def listenclient(self):
        self._serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._serversocket.bind((self._ip, self._port))
        self._serversocket.listen(self._max_block_size)
        print("server socket started")

    def accept(self):
        while self._runaccept:
            print("waiting for client connection")
            client, addr = self._serversocket.accept()
            self.processclient(client)
            self.processconnectedclient(client, 1)

    def processclient(self, client):
        thread = self._threadpool.popthread()
        th = thread(target=self.processclientrequest, args=(client,))
        th.start()
        print(client, " client is connected")

    def processclientrequest(self, client):
        data = client.recv(ConstantUtils.BUFFER_SIZE)
        print("receive data:", data)

        _news = News(0)
        _news.__dict__ = eval(data.decode(encoding='utf-8'))
        _news.print()
        _asknews = AskNews()

        if _news._newstype == 1:
            _asknews._status = True
            _asknews._message = "login success"
        else:
            _asknews._message = "option fail"
        self.processclientresponse(client, _asknews)
        self.processconnectedclient(client, 2)
        self._threadpool.pushthread()

    def processclientresponse(self, client, data):
        _data = str(data.__dict__)
        print("json obj to string data:", _data)
        time.sleep(self._replydelaytime)
        client.send(_data.encode("UTF-8"))

    def processconnectedclient(self, client, type):
        if type == 1:
            self._clients.append(client)
        elif type == 2:
            self._clients.remove(client)
        print("current connected client lenght->", self._clients.__len__())

    def close(self):
        self._runaccept = False
        self._serversocket.close()

def main():
    serverSocket = ServerSocket(ConstantUtils.IP, ConstantUtils.PORT)
    serverSocket._max_block_size = ConstantUtils.MAX_CONNECT
    serverSocket.start()
    time.sleep(20)
    serverSocket.close()

if __name__ == '__main__':
    main()
