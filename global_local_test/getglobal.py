#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

# import global_local_test.globalvar as gol
from global_local_test.global_class import GlobalTest

def test():

	gol = GlobalTest()
	# gol._init()
	# gol.set_value("ROOT",'123')
	print(gol.get_value('CODE'))

# if __name__ == '__main__':
#     test()