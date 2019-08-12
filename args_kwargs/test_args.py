#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"


def test():
	func_args(None)
	func_args(1,2)
	func_kwargs(a=1)

# 可以使用args1
def func_args(*args):
	print(args, type(args))
	# print(args[0])

def func_kwargs(**kwargs):
	print(kwargs,type(kwargs))

