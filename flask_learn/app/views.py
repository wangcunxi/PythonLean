#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/9/28 16:27
# Function
# @Author  : cunxi.wang
from flask import render_template

from flask_learn.app import app

@app.route('/',methods = ['GET', 'POST'])
def empty():
    return "Hello, World!"

@app.route('/index')
def index():
    empty = { 'nickname': 'wangcunxi','title':'Home' } # fake user
    listItem = [
        {'author': {'nickname': 'wangcunxi'},'body': 'one'},
        {'author': {'nickname': 'wangziqi'},'body': 'two'}
    ]
    return render_template("index.html",user = empty,listItem=listItem)