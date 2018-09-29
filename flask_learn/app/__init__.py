#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/9/28 16:24
# Function
# @Author  : cunxi.wang
from flask import Flask

app = Flask(__name__)
from app import views
