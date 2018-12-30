#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
你想使用 Unix Shell 中常用的通配符 (比如 *.py , Dat[0-9]*.csv 等) 去匹配文
本字符串
解决方案
fnmatch 模块提供了两个函数——fnmatch() 和 fnmatchcase() ，可以用来实现
这样的匹配。用法如下：
"""
from fnmatch import fnmatch, fnmatchcase

ret = fnmatch('foo.txt', '*.txt')
print(ret)
ret2 = fnmatch('foo.txt', '*?oo.txt')
print(ret2)
ret3 = fnmatch('Dat45.csv', 'Dat[0-9]*')
print(ret3)
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
ret4 = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(ret4)
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
addrs=[addr for addr in addresses if fnmatchcase(addr,'* ST')]
print(addrs)
addrs2=[addr for addr in addresses if fnmatchcase(addr,'54[0-9][0-9] *CLARK*')]
print(addrs2)