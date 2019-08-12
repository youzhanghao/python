#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

import pandas as pd


dfs = pd.DataFrame([[10, 0,-10], [10,1,-9],[10,20,10]], columns=[ 'score','test','test2'])
print(dfs)

# date_test = pd.date_range('2019-05-01','2019-05-30')
#
# date_da = date_test.dt.strftime('%Y/%m/%d')
# print(date_da.values)
# for day in date_da:
#     print("日期",day)
#
# print(dfs - dfs.shift(1).fillna(0))

s = pd.Series(pd.date_range('20130101 09:10:12', periods=4))
print(s)
print(s.dt.strftime('%Y/%m/%d'))
test_date = s.dt.strftime('%Y/%m/%d')
for day in test_date:
    print(day)