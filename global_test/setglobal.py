#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

# 注意当前文件用 . 引入 TODO from 或 import默认路径是从哪开始算的
# 文件夹名和文件名不要用关键字
import global_test.globalvar as gol

def test():

	gol._init()#先必须在主模块初始化（只在Main模块需要一次即可）


	#定义跨模块全局变量
	gol.set_value('CODE','UTF-8')
	gol.set_value('PORT',80)
	gol.set_value('HOST','127.0.0.1')
	gol.set_value('CONFIG_PATH','www')

# if __name__ == '__main__':
#     test()