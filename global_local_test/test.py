#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

# python中，每个函数都有一个自己的命名空间，叫做local namespace，它记录了函数的变量。
# python中，每个module有一个自己的命名空间，叫做global namespace，它记录了module的变量，包括 functions, classes 和其它imported modules，还有 module级别的 变量和常量。
# 还有一个build-in 命名空间，可以被任意模块访问，这个build-in命名空间中包含了build-in function 和 exceptions。
# 当python中的某段代码要访问一个变量x时，python会在所有的命名空间中寻找这个变量，查找的顺序为:
#
# local namespace - 指的是当前函数或者当前类方法。如果在当前函数中找到了变量，停止搜索
# global namespace - 指的是当前的模块。如果在当前模块中找到了变量，停止搜索
# build-in namespace - 如果在之前两个namespace中都找不到变量x，python会假设x是build-in的函数或者变量。如果x不是内置函数或者变量，python会报错NameError。
#
# 对于闭包来说，这里有一点区别，如果在local namespace中找不到变量的话，还会去父函数的local namespace中找变量。

# 使用import module时，module本身被引入，但是保存它原有的命名空间，所以我们需要使用module.name这种方式访问它的 函数和变量。
# from module import这种方式，是将其它模块的函数或者变量引到当前的命名空间中，所以就不需要使用module.name这种方式访问其它的模块的方法了。

from global_local_test.setglobal import test as testset
from global_local_test.getglobal import test as gettest
# import global_local_test.global_local_diiff
# from global_local_test.global_local_diiff import *
# from global_local_test.global_class import GlobalTest


if __name__ == '__main__':
	testset()
	gettest()
	# gol_wb = global_local_test.global_local_diiff.gols
	# gols = 'a'
	# gol_fm = gols
	# print(test_gol)
	# print("=============")
	# print(gol_fm["cc"])
	# # print(gol_w"cc"])
	# print("=============")
	# gol_ts = globals()
	# print(gol_ts)
	# gols = globals()
	# gols["cc"] = 'orange'
	# print(gols)
