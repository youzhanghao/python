# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:  Reworld


'readTextFile.py -- read and display text file'

fname = input('Enter filename:')
print()

# try-except-else用法
try:
    fobj = open(fname,'r')
except IOError as e:
    # 文件不存在已经包含在该异常内
    # 如何做文件名打印 file:%s  参考0609/string_.py
    print("*** file open error:", e)
else: # 此处else用法
    for eachLine in fobj:
        print(eachLine)
    fobj.close()