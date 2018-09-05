#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/21 17:55
# Python3.5
# @Author  : cunxi.wang
import select
import socket
import threading
import queue

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
    timeout = 1000
    messagequeues = {}
    READ_ONLY = (select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR)
    READ_WRITE = (READ_ONLY | select.POLLOUT)

    def __init__(self, ip, port):
        threading.Thread.__init__(self)
        self._ip = ip
        self._port = port
        self._threadpool = ThreadPool()

    def run(self):
        self.listenclient()
        self.accept()

    def listenclient(self):
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

    def accept(self):
        while self._runaccept:
            events = self.poller.poll(self.timeout)
            for fd, flag in events:
                s = self.fd_to_socket[fd]
                if flag & (select.POLLIN | select.POLLPRI):
                    if s is self._serversocket:
                        # A readable socket is ready to accept a connection
                        print("waiting for client connection")
                        connection, client_address = s.accept()
                        connection.setblocking(False)
                        self.fd_to_socket[connection.fileno()] = connection
                        self.poller.register(connection, self.READ_ONLY)
                        # Give the connection a queue to send data
                        self.messagequeues[connection] = queue.Queue()
                        self.processconnectedclient(connection,1)
                    else:
                        data = s.recv(1024)
                        if data:
                            self.messagequeues[s].put(data)
                            self.poller.modify(s, self.READ_WRITE)
                        else:
                            # Close the connection
                            self.poller.unregister(s)
                            s.close()
                            del self.messagequeues[s]
                elif flag & select.POLLHUP:
                    # A client that "hang up" , to be closed.
                    self.poller.unregister(s)
                    s.close()
                elif flag & select.POLLOUT:
                    # Socket is ready to send data , if there is any to send
                    try:
                        next_msg = self.messagequeues[s].get_nowait()
                    except queue.Empty:
                        # No messages waiting so stop checking
                        self.poller.modify(s, self.READ_ONLY)
                    else:
                        print(" sending %s to %s" % (next_msg, s.getpeername()))
                        self.processclientrequest(s,next_msg)
                elif flag & select.POLLERR:
                    # Any events with POLLERR cause the server to close the socket
                    s.close()
                    del self.messagequeues[s]

    def processclientrequest(self, client, data):
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

    def processclientresponse(self, client, data):
        _data = str(data.__dict__)
        print("json obj to string data:", _data)
        # time.sleep(self._replydelaytime)
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


if __name__ == '__main__':
    main()
