#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"


import pandas as pd
from pandas import DataFrame
df1=DataFrame({'a':[1,2,3], 'b':[4,5,6], 'key':[0,0,0]})
df2=DataFrame({'c':[3,2,1], 'd':[6,5,4], 'key':[0,0,0]})
data = pd.merge(df1, df2, on='key')
