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
from socketlean.test.thread.ClientThread import ClientThread
from socketlean.utils import ConstantUtils

def main():
    inputstr = raw_input('please input create client count:')
    while True:
        print(inputstr.isdigit())
        if inputstr.isdigit():
            break
        inputstr = raw_input('please input number type:')
    initclientcount = int(inputstr)
    while initclientcount > 0:
        thread = ClientThread('wangcunxi'+str(initclientcount),'wangcunxipassword'+str(initclientcount),ConstantUtils.IP,ConstantUtils.PORT)
        thread.start()
        initclientcount-=1
if __name__ == '__main__':
    main()