#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
怎样在一个序列上面保持元素顺序的同时消除重复的值？
解决方案
如果序列上的值都是 hashable 类型，那么可以很简单的利用集合或者生成器来解
决这个问题。比如：
"""


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(item)
def remove_repetition(somefile):
    with open(somefile,'r')as f:
        for line in dedupe(f):
            print(line)


if __name__ == '__main__':
    # a = [1, 5, 2, 1, 9, 1, 5, 10]
    # rets = dedupe(a)
    # print(list(rets))
    # for r in rets:
    #     print(r)
    a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    # print(list(dedupe2(a, key=lambda d:(d['x'], d['y']))))
    # print(list(dedupe2(a, key=lambda d: d['x'])))
    somefile=r"C:\Users\liming\Desktop\program\good_script\400W常用密码(整理).txt"
    remove_repetition(somefile)