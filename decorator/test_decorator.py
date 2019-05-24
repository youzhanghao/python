#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

''' 装饰器 测试 '''

import functools

def now():
	print("2019-05-22")

# python中一切皆对象
f = now
f()
print('11')
print("name: %s " % now.__name__)
print(f.__name__)
# 装饰器：一个包装函数的函数，它一般讲传入的函数或者类做一定的处理，返回修改之后的对象
# 能够在不修改原函数的基础上，在执行原函数前后执行的代码
# 常用场景 日志插入，事务处理，异常处理等
def log(func):
	@functools.wraps(func)  #  __name__ 复制到wrapper中
	def wrapper(*args,**kwargs):
		print("call %s():" % func.__name__)
		return func(*args, **kwargs)
	return wrapper

@log # 装饰器 == log(now_new)
def now_new():
	"""

	"""
	print('2019-05-22')
f_b = now_new
now_new()
log(now_new())
print(f_b.__name__) # @functools.wraps(func)

