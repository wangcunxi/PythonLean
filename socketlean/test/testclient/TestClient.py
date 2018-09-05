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

from pip._vendor.distlib.compat import raw_input
from socketlean.utils import ConstantUtils
from socketlean.clientsocket.ClientSocket import ClientSocket

def main():
    inputstr = raw_input('please input create client count:')
    while True:
        print('input is number->',inputstr.isdigit())
        if inputstr.isdigit():
            break
        inputstr = raw_input('please input number type:')
    initclientcount = int(inputstr)
    while initclientcount > 0:
        _clientsocket = ClientSocket(ConstantUtils.IP,ConstantUtils.PORT,'wangcunxi'+str(initclientcount),'wangcunxipassword'+str(initclientcount))
        _clientsocket.start()
        initclientcount-=1

if __name__ == '__main__':
    main()