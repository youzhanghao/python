#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

'''测试loguru模块'''

from loguru import logger
import sys


logger.debug("That's it,beautiful and simple logging")


# How to add a handler? How to setup logs formatting? How to filter messages? How to set level?
logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")

logger.info("this is info message")

logger.add("test_log_{time:YYYY-MM-DD}.log", backtrace=True, rotation = "500MB",)

logger.warning("this is waring message")

# logger.add(sys.stdout, colorize=True, format="<green>{time:YYYY-MM-DD at HH:mm:ss}</green> | {level} | {message}")

logger.info("this is color info message")
# TODO 日志多线程 验证  多线程安全
# logger.add("somefile.log", enqueue=True)
# 装饰器
name = r'/Users/youzhanghao/Desktop/python/python/test_loguru_{time:YYYY-MM-DD}.log'
logger.add(name, backtrace=True)  # Set 'False' to not leak sensitive data in prod

def func(a, b):
    return a / b

def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("What?!")

nested(0)
@logger.catch()
def logger_test(x):
	y = 1 / (x)
	raise Exception('error')
	return y

def test():
	logger_test(1)



# pretty log
