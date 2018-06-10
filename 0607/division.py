# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:  Reworld
# from __future__ import division

if __name__ == "__main__":
    # 现阶段地板除 未来移除
    print(1 / 2)  # 0  __future__  0.5
    print( 1 / 2.0) # 0.5
    # // 执行地板除  返回比真正商小的最小整数
    print( 1 // 2)  # 0
    print( -1 // 2)  # -1

    print( 1.0 % 3)
    # 浮点数的取余  x - (math.floor(x/y) * y)
    print( 4.8 % 3.2)
    # 优先级 **
    print(-3 ** 2)
    print((-3) ** 2)
    print(4**-1)

    print(-1-2) # -3
    print(0+1j**2) # -1+0j
    print(1+1j**2) # 0j
    print((1+1j)**2) # 2j

