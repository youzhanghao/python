# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:  Reworld

"""An example of reading and writing Unicode string:
write Unicode string to a file in utf-8 and read it back in"""

if __name__ == "__main__":
    CODEC = 'utf-8'
    FILE = 'tmp.txt'

    # 创建文件以utf-8格式书写
    hello_out = u"hello world"
    bytes_out = hello_out.encode(CODEC)
    f = open(FILE,'w')
    f.write(bytes_out)
    f.close()

    # 打开文件以utf-8格式读出
    f = open(FILE,'r')
    bytes_in = f.read()
    f.close()
    hello_in = bytes_in.decode(CODEC)
    print(hello_in)