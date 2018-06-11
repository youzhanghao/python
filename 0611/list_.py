# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:  Reworld

'''list for learning'''

def intList():
    # 列表的基本操作
    a_list = [123,'a',1-2j]
    b_list = ['abc',['1','2']]
    print(a_list[0])
    print(b_list[1][1])
    b_list[1] = 'a'
    print(b_list)
    b_list.append(['3',4])
    print(b_list)
    b_list.remove('a')
    print(b_list)
    # 123
    # 2
    # ['abc', 'a']
    # ['abc', 'a', ['3', 4]]
    # ['abc', ['3', 4]]

    # 列表比较 同字符串比较原理

    # 列表解析
    c_list = [i * 2 for i in [8, -2, '3']]
    print(c_list)
    # [16, -4, '33']
    d_list = [i for i in range(8) if i % 2 == 0]
    print(d_list)
    # [0, 2, 4, 6]

if __name__ == "__main__":
    intList()