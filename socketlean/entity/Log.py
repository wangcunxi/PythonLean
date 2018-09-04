#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/30 8:47
# Function
# @Author  : cunxi.wang

import time


class Log:
    _begintime = 0;
    _endtime = 0;

    def __init__(self):
        pass

    def notetime(self, type):   # 1:note begin time  2:note end time
        t = int(time.time())    # 秒级时间戳
        if (type == 1):
            self._begintime = t
        elif (type == 2):
            self._endtime = t
        else:
            print("note time type no exit")

    def print(self):
        begintime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self._begintime))
        endtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self._endtime))
        print("begin time->%s    end time->%s    time tifference->%ss" %(begintime ,endtime,(self._endtime - self._begintime)))
