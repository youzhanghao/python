#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

import pandas as pd


dfs = pd.DataFrame([[10, 0,-10], [10,1,-9],[10,20,10]], columns=[ 'score','test','test2'])
print(dfs)


print(dfs - dfs.shift(1).fillna(0))