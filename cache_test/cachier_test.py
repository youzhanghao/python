#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

from cachier import cachier
import datetime

@cachier(stale_after=datetime.timedelta(seconds=15))
def foo(arg1,arg2):
	return {'arg1':arg1, 'arg2':arg2}

if __name__ == '__main__':
	foo("test",'cache')