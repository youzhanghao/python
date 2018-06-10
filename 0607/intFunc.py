# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:  Reworld

if __name__ == "__main__":

    # 取绝对值
    print(abs(-1))
    print(abs(-1+1.0j))
    # 1
    # 1.41421356237

    # 自定义两个数值类型转换
    print(coerce(1,2))
    print(coerce(1.3, 13L))
    print(coerce(1,134L))
    print(coerce(1j,134L))
    # (1, 2)
    # (1.3, 13.0)
    # (1L, 134L)
    # (1j, (134 + 0j))

    # divmod()  返回包含商和余数的元组
    print(divmod(1,3))
    print(divmod(10,3))
    print(divmod(2.5,10))
    print(divmod(2+1j,0.5-1j))
    # (0, 1)
    # (3, 1)
    # (0.0, 2.5)
    # ((-0 + 0j), (2 + 1j))

    # pow() pow(x,y,z) 密码 做取余运算
    #     With two arguments, equivalent to x**y.  With three arguments,
    #     equivalent to (x**y) % z, but may be more efficient (e.g. for longs).
    print(pow(5,2,4))  # 1

    # round() 四舍五入 第二个参数精确位数
    print(round(3.4999,1))
    # 3.5
    print(round(-3.5)) # -4.0
    print(round(-3.4)) # -3.0


