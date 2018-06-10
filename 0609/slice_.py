# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:  Reworld

def cutLastChr(char="test"):
    """每次截取字符串最后一位输出"""
    if not isinstance(char, str):
        return
    i = -1
    for i in range(-1,-len(char), -1):  # 输出完整字符串  for i in [None] + range(-1,len(char),1)
        print(i)
        print(char[:i])


if __name__ == "__main__":
    test_char = 'abcde'
    print(test_char[0:-1])  # 左闭右开
    cutLastChr(test_char)

