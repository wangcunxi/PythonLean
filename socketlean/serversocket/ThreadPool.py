#!/usr/bin/env python
# -*- coding:utf-8 -*-
# File Name    : threadpool.py
# Author       : hexm
# Mail         : xiaoming.unix@gmail.com
# Created Time : 2017-03-23 20:03

import sys
import threading
import time


class ThreadPool(object):
    _listthread = []

    def __init__(self, initthreadnum=20, minthreadnum=5, maxthreadnum=30):
        self.initthreadnum = initthreadnum
        self.minthreadnum = minthreadnum
        self.maxthreadnum = maxthreadnum

    def popthread(self):
        if (self._listthread.__len__() < self.minthreadnum):
            for i in range(self.initthreadnum):
                self.pushthread()
        print("size  ", self._listthread.__len__())
        return self._listthread.pop()

    def pushthread(self):
        if (self._listthread.__len__() < self.maxthreadnum):
            self._listthread.append(threading.Thread)


def worke(pool, a1):
    time.sleep(1)
    print(a1)
    pool.pushthread()


def main():
    _threadpool = ThreadPool()

    for i in range(10000):
        thread = _threadpool.popthread()
        t = thread(target=worke, args=(_threadpool, i,))
        t.start()


if __name__ == '__main__':
    main()
