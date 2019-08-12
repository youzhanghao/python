#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

from kafka import KafkaProducer
import logging
logging.basicConfig(level=logging.DEBUG)

producer = KafkaProducer(bootstrap_servers='10.20.2.196:9092')
for _ in range(100):
    producer.send('foobar', b'some_message_bytes')