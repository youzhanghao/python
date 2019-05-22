#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

'''mysql为null插入  mysql 5.7版本后待验证？？？'''

def main():
	import pymysql

	conn = pymysql.connect(host="localhost", user="root", passwd="1234Ab..", db="test_python", charset="utf8mb4",port=3312)

	cur = conn.cursor()
	age = '18'
	name = 'lisi'
	date = 'null'
	sql = "insert into user (age,name,birth_date) values (%s, '%s', %s)" % (age,name,date)
	print('------单插入sql -------')
	print(sql)
	print('------批量插入sql ------')
	sql_many = "insert into user (age,name,birth_date) values (%s, '%s', %s)"
	print(sql_many)
	list = [(age,name,date)]
	sql_cai = "INSERT INTO sites (name, url,date) VALUES (%s, %s, %s)"
	list_b = [('18','zhangsan','null'),('21','wanger','2019-08-29')]
	print(list)
	# python None就是对应 mysql 的 null值
	val = [
		('Google', 'https://www.google.com',None),
		('Github', 'https://www.github.com','2019-08-29'),
		('Taobao', 'https://www.taobao.com','2019-08-29'),
		('stackoverflow', 'https://www.stackoverflow.com/','2019-08-29')
	]
	print(val)
	cur.executemany(sql_cai,val)
	# cur.execute(sql)


	cur.close()

	conn.commit()
	print(cur.rowcount,'记录表插入成功')


	conn.close()

if __name__ == '__main__':
    main()