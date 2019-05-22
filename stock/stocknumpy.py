#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

import numpy as np

def test():
	# standarnormal()
	# combine(2)
	pass


def standarnormal():
	# Important numpy中的数据处理是广播形式 并行处理 区别于Python中的list是作为一个整体处理
	# 200支股票
	stock_cnt = 200
	# 504天
	view_days = 504
	# 生成正态分布 均期望值=0，标准差=1的序列
	stock_day_change = np.random.standard_normal((stock_cnt,view_days))
	# 打印shape(200,504) 200行504列
	print(stock_day_change.shape)

	print(type(stock_day_change))
	# 打印出第一支股票，前5个交易日的涨跌幅情况
	print(stock_day_change[0:1, :5 ])
	# 打印倒数第一支，第二支 最后5个交易日的数据
	print(stock_day_change[-2: , -5: ])
	# 交易第一，第二天和倒数第一，第二天的数据
	first = stock_day_change[0:2, 0:5]
	end =  stock_day_change[-2:,-5:]
	print("前两天股票数据：%s， 后两天股票数据: %s " % (first, end))
	# 试试直接交换
	first,end = end,first
	print("交换后 --- 前两天股票数据：%s， 后两天股票数据: %s " % (first, end))
	# 数据转换与规整
	print(stock_day_change[0:2, 0:5])
	# 类型转换 只取整数
	print(stock_day_change[0:2,0:5].astype(int))
	# 保留2位小数
	print(np.round(first,2))
	# 使用Numpy中的nan_to_num填充na  pandas中的fillna()和dropna()函数更适合处理这种场景
	# 先copy一份数据，避免污染源数据
	test_tmp = first.copy()
	test_tmp[0][0] = np.nan
	print("前：%s" % test_tmp)
	test_tmp = np.nan_to_num(test_tmp)
	print("后：%s" % test_tmp)
	# 找出切片内涨幅超过0.5的股票时段
	mask = first > 0.5
	print("切片内涨幅超过0.5的: %s " % mask)
	test_tmp_b = first
	# first数组筛选对应的mask中index值为TRUE
	print("切片内涨幅超过0.5的股票时段 %s " % test_tmp_b[mask])
	# 在 np.array 索引中直接使用筛选条件
	tmp_test = end
	print('end: %s' % end)
	# print 跟单双引号没关系
	print('end筛选后: %s ' % (end[(tmp_test > 1) | (tmp_test < -1) ]))



def combine(a):
	# TODO 辨别 👇 未加括号的 会有什么情况
	# 分析
	a = -2
	if (a > 1 | (a < -1)):
		print('a在-1与1之外')
	else:
		print('-1<= a <=1')

if __name__ == '__main__':
	print('-----')
	combine(1)