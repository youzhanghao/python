#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

import numpy as np

def test():
	# 为0 shape填充
	print(np.zeros(2))
	# 为1shape填充
	print(np.ones((3,2),int))
	# 生成多维矩阵
	print(np.empty((2,3,3)))
	# 生成一维矩阵
	np_list = np.arange(3)
	print(np_list)
	print(np.ones_like(np_list))
	# 得到与np_list shape一样的矩阵
	print(np.zeros_like(np_list))
	# 对角线为1的矩阵
	print(np.eye(3))
