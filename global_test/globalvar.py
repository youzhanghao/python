#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"





def _init():#初始化
	global _global_dict
	_global_dict = {'config':'1'}


def set_value(key,value):
	""" 定义一个全局变量 """
	_global_dict[key] = value
	print(_global_dict)


def get_value(key,defValue=None):
	""" 获得一个全局变量,不存在则返回默认值 """
	try:
		print(_global_dict)
		return _global_dict[key]
	except KeyError as e:
		return

if __name__ == '__main__':
    pass
