# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:  Reworld


'readTextFile.py -- read and display text file'

fname = raw_input('Enter filename:')
print()

# try-except-else用法
try:
    fobj = open(fname,'r')
except IOError, e:
    # 文件不存在已经包含在该异常内
    # TODO 如何做文件名打印 file:%s
    print("*** file open error:", e)
else: # 此处else用法
    for eachLine in fobj:
        print(eachLine)
    fobj.close()