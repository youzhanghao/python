#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"


global_dict = {}

class GlobalTest(object):

	_global_dict = {}

	def __init__(self):
		print(global_dict)
		self._global_dict = global_dict


	def set_value(self, key, value):
		self._global_dict[key] = value

	def get_value(self,key):
		try:
			return self._global_dict[key]
		except Exception as e:
			print(e)

