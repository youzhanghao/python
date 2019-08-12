#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"
import pymysql


def process(i):
    tmp_str = i,
    return tuple(tmp_str)
    # return

# list_test = []
# record = ('来康镜标准版', '唐山新奥永顺清洁能源有限公司', ('1'), ('2500.00'))
# if record[0] in list_test:
#     print('yes')
# # print(list_test)
# tuple_test = (1,2,3)
# "ab","cd","ef" ==> (("ab",),("cd",),("ef",))
test="ab,cd,ef"
# test.split(",")
# print(map(lambda x:str(x),test.split()))
# test_str = "ab","ce","fg",
# test_str_one = "ab",
print(tuple(list(map(process,test.split(",")))))
# test_str_one_tupe = tuple(test_str_one)
# print(test_str_one_tupe)
# test_str_tupe = tuple(test_str)
# for i in test_str_tupe:
#     tmp_str = i,
#     tmp_str_tupe = tuple(tmp_str)
#     print(tmp_str_tupe)
# print(test_str_tupe)
# print(tuple(test_str_tupe))
# table_used="test"
# sql_field_info = 'select `column_name`, `column_comment` from information_schema.columns where table_name = "`' + table_used + '`"'
# print(sql_field_info)


#
# conn = pymysql.connect("10.19.248.200","ganjunfang" , "ganjunfang", "lk_open_core", charset='utf8', port=int(32048))
# cursor = conn.cursor()
# cursor.execute("select count(*) from lk_user_manage")
# print(cursor.fetchone()[0])

# black_table_list = ["a.b"]
# a = "a.b "
# if a in black_table_list:
#     print("yes")
# else:
#     print('No')