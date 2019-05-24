#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"



import notifiers

from loguru import logger

def test():
    # logger.debug("That's it,beautiful and simple logging")
    params = {
        "username": "youzhanghao003@gamil.com",
        "password": "28251100yzH",
        "to": "youzhanghao@ennew.cn"
    }

    # Send a single notification
    notifier = notifiers.get_notifier("gmail")
    print(notifier.required)

    notifier.notify(message='this is test message',to='youzhanghao003@gmail.com')
    notifier.notify(message="The application is running!", **params)

    # Be alerted on each error message
    from notifiers.logging import NotificationHandler

    handler = NotificationHandler("gmail", defaults=params)
    logger.add(handler, level="ERROR")