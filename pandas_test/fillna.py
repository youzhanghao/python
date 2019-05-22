#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

'''测试dataframe某些列为0填充，某些列为0000-00-00填充'''

import pandas as pd

dfs = pd.DataFrame([['a1', 1,'',''], ['a2', 4,]], columns=['uid', 'score','test','test2'])
col =['test']
print(dfs)
# 指定列删除
df1=dfs.drop(labels=col,axis=1)
print(df1)

df2=dfs[col].fillna('0000-00-00')
print(df2)

result=pd.concat([df1,df2],axis=1)
print(result)