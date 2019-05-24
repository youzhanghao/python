#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

import global_local_test.globalvar as gol

def test():

	gol._init()
	# gol.set_value("ROOT",'123')
	print(gol.get_value('config'))

# if __name__ == '__main__':
#     test()