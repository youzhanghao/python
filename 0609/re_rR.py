# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:  Reworld
import re

if __name__ == "__main__":
    # 原始字符串的使用 r或R
    m = re.search('\\[rtfvn]', r'hello world\n')
    if m is not None: print(m.group()) # 空
    m2 = re.search(r'\\[rtfvn]', r'hello world\n')
    if m2 is not None: print(m2.group()) # \n