#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"


from cache_test.local_cache_test import mem_cache
class Ebk5BookService(object):
    @mem_cache(7200,'',1000000000)
    def book_name_rel_id(self):
        '''
        书名与书籍ID映射关系
        '''
        # bk_list = Ebk5Book.mgr(ismaster=True).raw("select bookName,ID from ebk5_book")
        # return {i.get("bookName").lstrip('《').rstrip('》'):i.get("ID") for i in bk_list if i}
        return True
