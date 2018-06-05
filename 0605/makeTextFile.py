# coding=utf-8
# !/usr/bin/python

'makeTextFile.py -- create text file'

import os

ls = os.linesep # 本地变量别名

fname = raw_input("\nplease input filename\n")

all = []
print("\nEnter lines ('.' by itself to quit).\n")

while True:
    entry = raw_input(">")
    if entry == '.':
        break
    else:
        all.append(entry)

fobj = open(fname,'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print('DONE')
