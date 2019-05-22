#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"


def test():
	a = [ 1, 2, 3 ]
	b = a
	c = a[:]
	a[1] = 'change a '
	# 列表的copy  以及 % 格式化输出
	print("a is %s,b is %s,c is %s"% (a,b,c))
