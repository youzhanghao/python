# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:  Reworld

if __name__ == "__main__":
    str1 = 'abc'
    str2 = 'lmn'
    print(len(str1))
    print(max(str2),min(str2))
    # -1
    # -1
    # 3
    # ('n', 'l')

    for i,t in enumerate(str2):print(i,t)
    s,t = 'abc','123'
    print(zip(s,t))
    # (0, 'l')
    # (1, 'm')
    # (2, 'n')
    # [('a', '1'), ('b', '2'), ('c', '3')]

    if isinstance(u'\0xAb',str):
        print('true')
    else:
        print('false')

    # false
    # True

    print (chr(65)) # 0-255
    print (ord('A')) # 一个字符作为参数
    print (ord(u'\u2345'))
    # A
    # 65 ascii值
    # 9029 unicode数值