#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

'''测试读取配置文件'''

import configparser
import os

def test():
	config = configparser.ConfigParser()
	print('config:',config)
	config.read('test.conf',encoding='utf-8')

	# print('config:', config)
	secs = config.sections()
	print('节点:',secs)
	options = config.options('db')
	print('options:',options)
	val = config.get('db','db_port')
	print('val:',val)


	config_sql = configparser.ConfigParser()
	config_sql.read('test.sql')
	secs_sql = config_sql.sections()
	print('secs_sql',secs_sql)
	val_sql = config_sql.get('user','name_sql')
	print('val_sql',val_sql	)
	a = '1'
	print('')
if __name__ == '__main__':
    test()