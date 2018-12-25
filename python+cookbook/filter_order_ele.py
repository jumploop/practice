#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列
解决方案
最简单的过滤序列元素的方法就是使用列表推导。比如：
"""
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
li = [n for n in mylist if n > 0]
print(li)
pos = (n for n in mylist if n > 0)
# for x in pos:
# print(x)
# print(pos)
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
import math

my_ret = [math.sqrt(n) for n in mylist if n > 0]
print(my_ret)

clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)
clip_pos = [n if n < 0 else 0 for n in mylist]
print(clip_pos)

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress

more5 = [n > 5 for n in counts]
print(more5)
ret=list(compress(addresses,more5))
print(ret)

