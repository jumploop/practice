#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只
"""
for x in range(20):
    for y in range(33):
        z = 100 - x - y
        if x * 5 + y * 3 + z / 3 == 100:
            print('公鸡：%d只，母鸡：%d只，小鸡：%d只' % (x, y, z))
#  要理解程序背后的算法 - 穷举法
