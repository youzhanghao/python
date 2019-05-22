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

logger.add("test_log_{time}.log")

logger.warning("this is waring message")



@logger.catch()
def logger_test(x):
	return 1 / (x)

def test():
	logger_test(0)

