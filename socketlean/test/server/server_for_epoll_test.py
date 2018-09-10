#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/30 8:36
# @Author  : cunxi.wang

import sys
import os
projectroot = os.path.abspath('..')
print(projectroot)
sys.path.append(projectroot)
print(sys.path)

from socketlean.server_socket.server_socket_for_epoll import ServerSocket
from socketlean.utils import constant_utils

# 主入口
def main():
    serverSocket = ServerSocket(constant_utils.IP, constant_utils.PORT)
    serverSocket.start()

if __name__ == '__main__':
    main()