#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

''' loguru 日志类封装 '''
from loguru import logger
import os
import configparser

# 日志配置
CONFIG_LOG_PATH = os.path.join(os.path.abspath('.'),'loguru.conf')
log_config = configparser.ConfigParser()
log_config.read(CONFIG_LOG_PATH,encoding='utf-8')
print(log_config)
log_path = os.path.join(os.path.abspath('..'),log_config.get('dev','log.path'))
name = os.path.join(log_path,log_config.get('dev','log.name'))
backtrace = log_config.get('dev','log.backtrace')
class Loguru(object):

	_log = None

	# 读取日志配置
	def __init__(self):
		# name = 'test_loguru_{time:YYYY-MM-DD}.log'
		print(name)
		# name_b = '/Users/youzhanghao/Desktop/python/python/test_loguru/test_loguru_{time:YYYY-MM-DD HH-mm-ss}.log'
		logger.add(name , backtrace=backtrace)
		self._log = logger

	def debug(self,msg):
		self._log.debug(msg)

	def info(self,msg):
		self._log.info(msg)

	def get_logger(self):
		return self._log

@logger.catch()
def test(x):
	return 1 / (x)
if __name__ == '__main__':
	loguru_test = Loguru()
	loguru_test.info('this is self info')
	loguru_test.get_logger().warning('this is warning message')
	test(0)