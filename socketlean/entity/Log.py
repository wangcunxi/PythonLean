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
    def notetime(self,type):                # 1:记录开始时间  2:记录结束时间
        t = int(time.time())                #原始时间戳
        if(type==1):
            self._begintime = t             #秒级时间戳
        elif(type==2):
            self._endtime = t               #秒级时间戳
        else:
            print("记录时间类型不存在")
    def print(self):
        begintime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self._begintime))
        endtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self._endtime))
        print('开始时间',begintime,'   结束时间',endtime,'   时间差',(self._endtime-self._begintime))