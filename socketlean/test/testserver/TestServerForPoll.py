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

from socketlean.serversocket.ServerSocketForPoll import ServerSocket
from socketlean.utils import ConstantUtils

# 主入口
def main():
    serverSocket = ServerSocket(ConstantUtils.IP, ConstantUtils.PORT)
    serverSocket.start()

if __name__ == '__main__':
    main()