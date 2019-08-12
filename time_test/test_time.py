#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

import time

def test():
    print (time.strftime('%H:%M:%S',time.localtime(time.time())))

if __name__ == '__main__':
    test()