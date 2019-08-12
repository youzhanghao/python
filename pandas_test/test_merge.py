#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

import pandas as pd

def test():
    info=[['time','公司','客户','sore'],['2019-05-19',4,5,6],['2019-05-17',7,8,9],['2019-05-15',4,5,6],['2019-05-13',7,8,9]]
    info2=[['time','公司','客户','sore'],['2019-05-16',4,5,0],['2019-05-15',7,8,0],['2019-05-14',4,5,0],['2019-05-13',7,8,0]]
    df = pd.DataFrame(info[1:],columns=info[0])
    df2 = pd.DataFrame(info2[1:],columns=info[0])
    print(df)
    print(df2)

    result= pd.merge(df, df2, on=['time', '公司', '客户'], how='outer').fillna(0)
    print(type(result))
    print(result)
    result['sore']=result['sore_x']+result['sore_y']
    result=result.drop(['sore_x','sore_y'],axis=1)
    print(result.sort_values(by ='time'))

def test_b():
    # 流水表
    org_turnover = [('流水时间','公司','商品名','销售额','销售数量'),('2019-05-19','来康','来康镜',500,6),('2019-05-17','支付宝','平衡称',200,9)]
    # 公司
    org_company = [['公司'],['来康'],['支付宝']]
    # 商品名
    org_product = [['商品名'],['来康镜'],['平衡称']]
    # 时间
    org_time = [['流水时间'],['2019-05-17'],['2019-05-18'],['2019-05-19']]
    # 根据公司名 商品名 时间 生成新的Df
    # df2 = pd.merge(org_company,org_product,org_time)
    # print(df2)
    # 公司和商品名和时间做笛卡尔积
    # df_org_turnover无[流水时间,公司名,产品名]则做0填充
    df_org_turnover = pd.DataFrame(org_turnover[1:],columns=org_turnover[0])
    df_org_company = pd.DataFrame(org_company[1:],columns=org_company[0])
    df_org_product = pd.DataFrame(org_product[1:],columns=org_product[0])
    df_org_time =  pd.DataFrame(org_time[1:],columns=org_time[0])
    df_org_company['value'] = 1
    df_org_product['value'] = 1
    df_org_time['value'] = 1
    # 先处理原始数据
    # 后对数据做填充处理
    # 笛卡尔积
    # date_time = pd.date_range('2019-05-01','2019-05-30')
    df_company_product = pd.merge(df_org_company, df_org_product,how='left',on='value')
    print(df_company_product)
    df_company_product_time = pd.merge(df_company_product,df_org_time,how='right',on='value')
    print(df_company_product_time)
    del df_company_product_time['value']
    print(df_company_product_time)
    # 原始数据补0
    result = pd.merge(df_company_product_time,df_org_turnover, on=['流水时间', '公司', '商品名'], how='outer').fillna(0)
    print(result.count())

    print(result)
    # result = pd.merge(df_org_time,df_org_company,df_org_product)
    # result_gp = result.set_index(['流水时间', '公司', '商品名'])
    print(result.groupby(['流水时间', '公司', '商品名']).sum().reset_index(['流水时间', '公司', '商品名']))
    # print(2)


