# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:  Reworld


'''特殊符号说明'''
#  没有缩进 称为主体
if __name__ == "__main__":

    # 使用 \ 换行  \ 后 不可跟注释
    a = 2
    # 首行以关键字开始 以冒号结束 该行之后构成代码组  代码组合首行构成子句 clause
    # 使用缩进体现代码层次，同一码组必须严格左对齐
    if (a > 1) and \
        a < 3 :
        # 使用'''语句块不用 \ 换行
        print( '''hello this
        is block,
        ....''')
    # 使用闭合操作符，小括号，中括号，花括号  不用 \ 换行  同时注意Python变量的赋值多样性
    # 推荐使用括号替代 \ 做换行  可读性更好
    go_surf, get_a_tan_while, boat_size, toll_money = (1, # 此处可带注释
                        'windsurfing',40.0, -2.00)

