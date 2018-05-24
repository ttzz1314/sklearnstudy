#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from showutil import *
from utils.logutil import *
from foo import *

su = ShowUtil()
lu = LogUtil()

su.show()
lu.log()

f2 = Foo2('zhouzhi')

f2.hi()

Foo.count = 3000
print(Foo.count)
print(f2.__class__.count)

f2.showCount()
f2.hi()