#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

class A(object):
	pass

print(callable(A))
a = A()
print(callable(a))

class B(object):

	def call_func(self,func_name):

		# self.eval(func_name)()
		pass

	def test_func(self):
		print("call this func")


	def __call__(self, *args, **kwargs):
		print("instances are callable now")

print(callable(B))
b = B()
print(callable(b))
b()
c = "test_func"
# b.call_func(c)