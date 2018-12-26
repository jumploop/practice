#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
现在有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某
些操作，比如查找值或者检查某些键是否存在。
解决方案
假如你有如下两个字典
"""
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
from collections import ChainMap
c=ChainMap(a,b)
print(c)
print(c['x'])
print(c['y'])
print(c['z'])
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged=dict(b)
d=merged.update(a)
print(merged)
