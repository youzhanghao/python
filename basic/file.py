# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:  Rewrite

if __name__ == "__main__":
    try:
        handle = open("tmp.txt","w")
        handle.write("hello")
        handle.close()
        fileObj = open("tmp.txt",'r')
        for ecahLine in fileObj:
            print(ecahLine)
        fileObj.close()
    except IOError,e:
        print('file open error: ',e)
