#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"


''' 
    1. 扫描数据实例全库全表字段充盈度
'''
import xlwt
import pymysql

def export(host,user,password,dbname,table_name,outputpath,port):
    conn = pymysql.connect(host,user,password,dbname,charset='utf8',port=port)

    # conn = pymysql.connect(host="", user="root", passwd="1234Ab..", db="demo", charset="utf8mb4",
    #                        port=30166)

    # 获取所有表
    # 获取表的所有字段和总的行数
    # 获取字段的名称和空的行数 计算充盈度
    # pymysql 操作流程 获取conn,通过conn获取游标对象cursor,cursor执行sql语句(这一步有真正执行么？有全表扫描么)
    # cursor.execute返回受影响的行数，并且cursor似乎拿到了所有的信息了

    cursor = conn.cursor()
    print("获取服务器信息:",conn.get_server_info())

    sql_databases = 'show databases'
    sql_tables = "show tables"
    db_used = "filling_degree"

    count = cursor.execute(sql_databases)
    all_databases = cursor.fetchall()
    print('总计数据库数量:%s 数据库集:%s'% (count,all_databases))

    conn.select_db(db_used)
    count = cursor.execute(sql_tables)
    all_tables = cursor.fetchall()
    print('总计表数量:%s 表集:%s' %(count, all_tables))

    table_used = "test_user_two"
    sql_table = 'select * from ' + table_used
    count = cursor.execute(sql_table)

    fields = cursor.description
    fields_list = []
    # TODO 查看哪个sql更适合
    field_degree_dict = {}

    # # 写上字段信息
    for i in range(0, len(fields)):
        # sheet.write(0,field,fields[field][0])
        if len(fields) > 100:
            print("warning")
        field = fields[i][0]


        sql_empty = "select " + field + " from " + table_used + " where "+ field +" is null"
        print(sql_empty)
        empty_rows = cursor.execute(sql_empty)
        filling_degree = round((int(count) - int(empty_rows))/(int(count)),2)
        field_degree_dict[field] = filling_degree
        # print(field_degree_dict)
    fields_list.append(field_degree_dict)
        # print(fields_list)




    print('%s表总计%s字段,字段集:%s' %(table_used,len(fields),fields_list))
    table_field_dict = {table_used:fields_list}
    print("table结果集:%s" %(table_field_dict))


    return


    sql = 'select * from '+table_name
    print(sql)
    count = cursor.execute(sql)
    print(cursor.fetchall())
    # conn.query("select count(*) from " + table_name)
    # print(conn.query("select count(*) from " + table_name))
    print("count:",count)
    # 重置游标的位置
    cursor.scroll(0,mode='absolute')
    # 搜取所有结果


    # results = cursor.fetchall()

    # print("result:",results)


    # 获取MYSQL里面的数据字段名称
    fields = cursor.description
    print("fields:",fields)

    # workbook = xlwt.Workbook()
    # sheet = workbook.add_sheet('table_'+table_name,cell_overwrite_ok=True)
    #
    # # 写上字段信息
    for field in range(0,len(fields)):
        # sheet.write(0,field,fields[field][0])
        print(fields[field][0])
    # # 获取并写入数据段信息
    # row = 1
    # col = 0
    # for row in range(1,len(results)+1):
    #     for col in range(0,len(fields)):
    #         sheet.write(row,col,u'%s'%results[row-1][col])
    #
    # workbook.save(outputpath)


# 结果测试
if __name__ == "__main__":
    # export('localhost','root','1234Ab..','demo','lk_sales_user_test',r'datetest.xlsx')
    # export('10.19.248.200','laikang','123Ab..','test_filling_degree','test_user_two',r'datetest.xlsx',30166)
    export('10.19.248.200','laikang','123Ab..',None,None,r'datetest.xlsx',30166)




