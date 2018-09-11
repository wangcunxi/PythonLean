#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/21 17:55
# Python3.5
# @Author  : cunxi.wang

import socket
import threading
import time

from socketlean.entity.request_message import RequestMessage
from socketlean.entity.respone_message import ResponseMessage
from socketlean.server_socket.thread_pool import ThreadPool
from socketlean.utils import constant_utils


class ServerSocket(threading.Thread):
    _max_block_size = constant_utils.MAX_CONNECT
    _replydelaytime = constant_utils.DELAYTIME
    _runaccept = True
    _threadpool = ""

    def __init__(self, ip, port, ):
        threading.Thread.__init__(self)
        self._ip = ip
        self._port = port
        self._threadpool = ThreadPool()

    def run(self):
        self.start_server()

    def start_server(self):
        self._serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._serversocket.bind((self._ip, self._port))
        self._serversocket.listen(self._max_block_size)
        print("server socket started")	
        self.wait_accept()

    def wait_accept(self):
        while self._runaccept:
            print("waiting for client connection")
            client, client_address = self._serversocket.accept()
            thread = self._threadpool.popthread()
            th = thread(target=self.__process_client_message, args=(client,))
            th.start()
            print(client, " client is connected")

    def __process_client_message(self, client):
        data = client.recv(constant_utils.BUFFER_SIZE)
        print("receive data:", data)
        _request_message = RequestMessage(0)
        _request_message.__dict__ = eval(data.decode(encoding='utf-8'))
        _request_message.print()
        _response_message = ResponseMessage()

        if _request_message._message_type == 1:
            _response_message._status = True
            _response_message._data = "login success"
        else:
            _response_message._data = "option fail"

        _data = str(_response_message.__dict__)
        print("json obj to string data:", _data)
        time.sleep(self._replydelaytime)
        try:
            client.send(_data.encode("UTF-8"))
        except Exception as e:
            print("exception e:", e)
        finally:
            self._threadpool.pushthread()

    def close(self):
        self._runaccept = False
        self._serversocket.close()


def __test_self():
    _serverSocket = ServerSocket(constant_utils.IP, constant_utils.PORT)
    _serverSocket._max_block_size = constant_utils.MAX_CONNECT
    _serverSocket.start()
    time.sleep(120)
    _serverSocket.close()


if __name__ == '__main__':
    __test_self()
