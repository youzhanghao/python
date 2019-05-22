#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

'''super和__init__区别'''


class base():
	def __init__(self):
		print('base create')

class child_a(base):
	def __init__(self):
		print('create A')
		base.__init__(self)

class child_b(base):
	def __init__(self):
		print('create B')
		super(child_b,self).__init__()

if __name__ == '__main__':
	base()
	a = child_a()
	b = child_b()