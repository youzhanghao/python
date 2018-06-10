# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:  Reworld

if __name__ == "__main__":
    print(type(""))
    print(type(100))
    print(type(1.0))
    print(type([]))
    print(type(()))
    print(type({}))
    print(type(type))

    class Foo: pass

    foo = Foo()
    print(type(Foo))
    print(type(foo))

    class Bar(object):pass

    bar = Bar()

    print(type(Bar),type(bar))
