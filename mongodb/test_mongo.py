#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

from pymongo import MongoClient
import datetime
from urllib.parse import quote_plus
import pprint

client = MongoClient("mongodb://presto:presto123..@10.20.2.196:27018")
db = client['test_demo']
posts = db.posts
def test_demo_one():
# user = 'presto'
# password = 'presto123..'
# user = 'admin'
# password = '123Ab..'
# socket_path = 'presto'
# uri = "mongodb://%s:%s@%s" % (
#     quote_plus(user), quote_plus(password), quote_plus(socket_path))
# client = MongoClient(uri)
#     client = MongoClient("mongodb://admin:123Ab..@10.20.2.196:27018/")
    # db = client.test_database
    # db = client['test_demo']
    # print(db.collection_names())
    post = {"author": "Mike","text": "My first blog post!","tags": ["mongodb", "python", "pymongo"],"date": datetime.datetime.utcnow()}
    # posts = db.posts
    # post_id = posts.insert_one(post).inserted_id
    print(111)
    print(db.list_collection_names())
    # print(post_id)
    pprint.pprint(posts.find_one())
    # print(posts.find_one())
def test_demo_two():
    new_posts = [{"author": "Mike","text": "Another post!","tags": ["bulk", "insert"],
    "date": datetime.datetime(2009, 11, 12, 11, 14)},{"author": "Eliot","title": "MongoDB is fun",
    "text": "and pretty easy too!",
    "date": datetime.datetime(2009, 11, 10, 10, 45)}]
    result = posts.insert_many(new_posts)
    pprint.pprint(result.inserted_ids)

def test_demo_three():
    for post in posts.find():
        pprint.pprint(post)
    for post in posts.find({'author':"Mike"}):
        pprint.pprint(post)
    print(posts.count_documents({}))
    print(posts.count_documents({"author":"Mike"}))
    d = datetime.datetime(2019,11,12,12)
    for post in posts.find({"date":{"$lt":d}}).sort("author"):
        pprint.pprint(post)


if __name__ == '__main__':
    test_demo_one()