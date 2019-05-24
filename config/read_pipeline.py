#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

'''测试读取配置文件'''

import configparser
import os
# from test_loguru.loguru_util import Loguru
from loguru import logger
def test():
	config = configparser.ConfigParser()
	# print('config:',config)
	config.read('pipeline.conf',encoding='utf-8')
	b = 'a,b'
	# print('config:', config)
	# 找到pipeline
	pipelines = str(config.get('pipelines','pipelines')).split(',')
	print(pipelines)
	# logger = Loguru()
	# 找到每个pipeline中的job
	for pipeline in pipelines:
		jobs = str(config.get('jobs',pipeline)).split(',')
		print(jobs)
		for job in jobs:
			logger.info("jos is %s " % job)
			stages = eval(config.get('stage',job))
			for stage in stages:
				process = dict(stage)["processor"]
				operator = dict(stage)["operator"]
				print(process,operator)




	print('--- done --- ')


if __name__ == '__main__':
    test()