#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/21 17:58
# Python3.5
# @Author  : cunxi.wang

import socket
import threading

from socketlean.entity.log import Log
from socketlean.entity.request_message import RequestMessage, LoginData
from socketlean.entity.respone_message import ResponseMessage
from socketlean.utils import constant_utils

class ClientSocket(threading.Thread):
    _ip = ""
    _port = ""
    __log = Log()
    def __init__(self, ip, port, username, password):
        threading.Thread.__init__(self)
        self._ip = ip
        self._port = port
        self._username = username
        self._password = password

    def run(self):
        try:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create client socket
            self._socket.connect((self._ip, self._port))
            print("connected to server...")
            self.send_messge()
            self.recv_message()
        except Exception as e:
            print("disconnect to server...")

    def send_messge(self):
        _login_data = self.__get_login_date(self._username, self._password)
        _login_data.print()
        _data = str(_login_data.__dict__)
        print("json obj to string data:", _data)
        try:
            self.__log.note_time(1)  # note send message begin time
            self._socket.send(_data.encode("UTF-8"))
        except Exception as e:
            print("client exception e:",e)
            return False
        return True
    def recv_message(self):
        _data = self._socket.recv(constant_utils.BUFFER_SIZE)
        print("receive data:", _data)
        self.__log.note_time(2)  # note receiver response message from server
        self.__log.print()
        _response_message = ResponseMessage()
        _response_message.__dict__ = eval(_data.decode(encoding='utf-8'))
        _response_message.print()
        # if _response_message._status:
        #     pass
        # else:
        #     pass
        self.close()
    def __get_login_date(self, username, password):
        _login_message = LoginData(username, password)
        _request_message = RequestMessage(1)
        _request_message._data = str(_login_message.__dict__)
        return _request_message

    def close(self):
        self._socket.close()


def test_self():
    _client_socket = ClientSocket(constant_utils.IP, constant_utils.PORT, "username", "password")
    _client_socket.start()

if __name__ == '__main__':
    test_self()
    '''
    quitNum = raw_input('press Nubmer to exit:')
    while True:
      if quitNum.isdigit():
         break
      quitNum = raw_input('press Nubmer to exit:')
    '''
