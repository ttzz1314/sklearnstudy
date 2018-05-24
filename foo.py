#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Foo:
    count = 10

    def __init__(self, name):
        self.name = name

    def hi(self):
        print(self.name + '， 你是第%i个访问者'%self.__class__.count)

    @staticmethod
    def showCount():
        print('count = ' + str(Foo.count))

    @classmethod
    def showName(cls):
        print(cls.name + ', welcome!')

class Foo2(Foo):
    def hi(self):
        print('Foo2实例准备调用父类的方法....')
        super(Foo2, self).hi()