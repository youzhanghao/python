#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

import pandas as pd
import numpy as np

def test():

	# dates = pd.date_range('20130101',periods=6)
	dates = pd.date_range('20130101', periods=6)
	dates_b = pd.date_range('20190519', periods=30,freq='1M')
	print(dates_b)

	# print(dates)
	# df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list['ABCD'])
	# print(np.random.randn(6,4))
	# df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list['ABCD'])  中括号
	df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
	print(df)
	print('------------')
	ses = pd.Series(1,index=list(range(4)),dtype='float32')
	# print(ses)
	# 读取头部
	df_1 = df.head(1)
	print(df_1)
	# 读取尾部
	df_2 = df.tail(3)
	print(df_2)
	# 读取索引
	print(df.index)
	# 读取列
	print("列"+df.columns)
	df.to_numpy()
	# 多数据类型 转 numpy花销大
	print(df.to_numpy())
	# 静态总结  一些统计数据  各个含义？？？
	print(df)
	print('-------')
	print(df.describe())
	# 翻转
	df_t = df.T
	print(df_t)
	print(df_t.columns)
	print(df.sort_index(axis=1,ascending=False))
	print("第0行 %s" % dates[0])
	print(df.loc[dates[0]])


if __name__ == '__main__':
    test()
