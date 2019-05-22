# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:  Reworld

"""check num type"""

def checkNumType(num):
    print (num,"is"),
    if isinstance(num, (int, float, complex)):
        print ('a number of type:', type(num).__name__)
    else:
        print ('not a number at all!')

if __name__ == "__main__":
    checkNumType(5)
