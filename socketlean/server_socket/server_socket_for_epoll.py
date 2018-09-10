#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/21 17:55
# Python3.5
# @Author  : cunxi.wang
import select
import socket
import threading

from socketlean.entity.respone_message import ResponseMessage
from socketlean.entity.request_message import RequestMessage
from socketlean.server_socket.thread_pool import ThreadPool
from socketlean.utils import constant_utils


class ServerSocket(threading.Thread):
    _ip = ""
    _port = ""
    _max_block_size = constant_utils.MAX_CONNECT
    _replydelaytime = constant_utils.DELAYTIME
    _runaccept = True
    _epoll_timeout = 1000
    READ_ONLY = (select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR)

    def __init__(self, ip, port):
        threading.Thread.__init__(self)
        self._ip = ip
        self._port = port
        self._threadpool = ThreadPool()

    def run(self):
        self.__start_server()
        self.__proccess_poll_event()
    def __self_server(self):
        self._serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._serversocket.bind((self._ip, self._port))
        self._serversocket.listen(self._max_block_size)
        self._serversocket.setblocking(False)
        # Set up the poller
        self.poller = select.poll()
        self.poller.register(self._serversocket, self.READ_ONLY)
        # Map file descriptors to socket objects
        self.fd_to_socket = {self._serversocket.fileno(): self._serversocket, }
        print("server socket started")

    def __proccess_poll_event(self):
        while self._runaccept:
            events = self.poller.poll(self._epoll_timeout)
            for index, flag in events:
                print(index,flag)
                _socket = self.fd_to_socket[index]
                if flag & (select.POLLIN | select.POLLPRI):
                    if _socket is self._serversocket:# A readable socket is ready to accept a connection
                        print("waiting for client connection")
                        client, client_address = _socket.accept()
                        client.setblocking(False)
                        self.fd_to_socket[client.fileno()] = client
                        self.poller.register(client, self.READ_ONLY)
                    else:
                        try:
                            data = _socket.recv(1024)
                            if data:
                                self.__process_client_message(_socket,data)
                            else:
                                raise Exception("receive data is null mean client connect error")
                        except Exception as e:
                            print("exception e:",e)
                            self.__unregister_client(_socket)
                elif (flag & select.POLLHUP) or (flag & select.POLLERR):
                    # A client that "hang up" andAny events with POLLERR cause the server to close the socket
                    self.__unregister_client(_socket)
    def __unregister_client(self,client):
        self.poller.unregister(client)
        client.close()
    def __process_client_message(self, client, data):
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
        client.send(_data.encode("UTF-8"))

    def close(self):
        self._runaccept = False
        self._serversocket.close()

def test_self():
    _server_socket = ServerSocket(constant_utils.IP, constant_utils.PORT)
    _server_socket._max_block_size = constant_utils.MAX_CONNECT
    _server_socket.start()

if __name__ == '__main__':
    test_self()