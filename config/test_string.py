#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

class Test(object):

	_func = None

	def mul(self,x):
		return x * x

	def run_name(self,func):
		self._func = eval(func)
		self._func()

def test():
	test_str = '[{"processor":"exceldatatomysql","operator":""},{"processor":"exceldatatomysql","operator":""}]'
	print(list(test_str))
	print(eval(test_str))
	test_func = 'mul'
	test_class = Test()

	# func = eval(test_func)
	# print(func)
	print(test_class.test_func(2))

