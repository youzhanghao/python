# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:  Rewrite



if __name__ == "__main__":
    foo = 'abc'
    for i in range(len(foo)):
        print foo[i], '(%d)' % i

    for i, ch in enumerate(foo):
        print ch, '(%d)' % i

    sqdEvens = [x ** 2 for x in range(8) if not x % 2]