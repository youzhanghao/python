# coding:utf-8

#    __author__ = '郭 璞'
#    __date__ = '2016/8/22'
#    __Desc__ = 测试文件
# import excel_mysql.xlsx2sql as xls
# 注意如果是使用 __main__ 且使用该文件为入口文件  则引入. 以当前为入口了 理解__main__的原理
# from import 尽量不使用相对路径
from excel_mysql.xlsx2sql import XlsxTool, Xlsx2sql

def test():

	print('-----s-----------------------------\n')

	tool = XlsxTool()
	# table_header_type = ['varchar(100) not null','int(100) ','varchar(255)','varchar(100)']
	table_header_type = ['int(100) not null comment "主键" ','varchar(255) ','varchar(255)','varchar(255)','varchar(30)','varchar(30)','varchar(100) not null']
	release = Xlsx2sql(tool)
	release.generate(r'/Users/youzhanghao/Desktop/python/python/excel_mysql/readout.xlsx',table_header_type,"id",r'./readout.sql')


if __name__ == '__main__':
	test()
