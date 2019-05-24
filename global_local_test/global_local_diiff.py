#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"


''' 
	global 和 local 所存储的空间和内存
	global：全局命名空间
	local: 局部命名空间
'''

def func(a = 1):
	b = 2
	print("内置函数 %s" % locals())
	locs = locals()
	locs["c"] = -1
	print(locs["c"])
	print("内置函数 %s" % locals())
	return a + b

func()

test_gol = 'hhhhhh'
print(globals())
gols = globals()
gols["cc"] = 'orange'
print(gols)

