# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:  Reworld

if __name__ =="__main__":

    # 普通赋值
    anInt = -12
    aString = 'cart'
    aFloat = -3.14
    anotherString = 'shop' + 'ping'
    aList = [3.14e10, '2']
    # 增量赋值
    m = 12
    m %= 7
    m **= 2
    print(m)
    # 多重赋值
    x = y = z = 1
    # 多元赋值
    (x,y) = ("a","b")
    # 值交换
    (x,y) = (y,x)
    print(y,x)
