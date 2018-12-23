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

if __name__ == '__main__':
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    rets=dedupe(a)
    print(list(rets))
    # for r in rets:
    #     print(r)