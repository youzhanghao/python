# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:  Reworld

# (1) 起始行 ⬆

#（2）模块文档
"this is a templete module"

# (3) 模块导入
import sys
import os

# (4) (全局)变量定义
debug = True

# (5) 类定义(若有)
class FooClass(object):
    "Foo Class"
    pass

# (6) 函数定义(若有)
def test():
    "test function"
    foo = FooClass()
    if debug:
        print("ran test()")
    pass
# (7) 主程序
if __name__ == "__main__":
    test()

