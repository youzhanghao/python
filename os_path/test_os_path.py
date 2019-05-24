#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

''' os path 路径测试 '''

import os

def test():
	AIR = 'local'
	path = os.environ.get('AIR') if os.environ.get('AIR') is not None else AIR
	print(path)
	print(os.path)
	print('当前工作目录路径: %s ' % os.getcwd())
	print('当前工作目录的绝对路径: %s ' % os.path.abspath('..'))
	print('当前工作目录路径: %s ' % os.path.curdir)
