# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:  Rewrite

if __name__ == "__main__":

    print(2 == 2)
    print(2.46 <= 2)
    # print(5+4j < 2 -3j)  报错
    print([3, 'abc'] == ['abc', 3])

    # 多个比较操作放在同一行进行，求值顺序从左到右
    print(3 < 4 < 5)
    print(3 > 2 > 5 !=2)

    foo1 = 4.3
    foo2 = foo1
    foo3 = 4.3
    foo4 = 1 + 3.3
    print(id(foo1),id(foo2),id(foo3),id(foo4))
    # (140480586453024, 140480586453024, 140480586453024, 140480584254600)

    foo5 = 1
    foo6 = 1
    if (foo5 is foo6):
        print("same obj")
    else:
        print("diff obj")
