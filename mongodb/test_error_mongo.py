#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"
from pymongo import MongoClient

conn_url = "mongodb://presto:presto123..@10.20.2.196:2701"
client = MongoClient("mongodb://presto:presto123..@10.20.2.196:2701")
print(client)
db = client['test_demo']


def test():
    conn_url = "mongodb://presto:presto123..@10.20.2.196:2701"
    client = MongoClient("mongodb://presto:presto123..@10.20.2.196:2701")
    print(client)

