#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/30 8:36
# @Author  : cunxi.wang

import time
from socketlean.serversocket.ServerSocket import ServerSocket
from socketlean.utils import ConstantUtils


# 主入口
def main():
    serverSocket = ServerSocket(ConstantUtils.IP, ConstantUtils.PORT, ConstantUtils.MAX_CONNECT,ConstantUtils.DELAYTIME)
    serverSocket.startserversocket()
    # time.sleep(600)
    # serverSocket.stopserversocket()

if __name__ == '__main__':
    main()