#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
你的程序已经出现一大堆已无法直视的硬编码切片下标，然后你想清理下代码。
解决方案
假定你有一段代码要从一个记录字符串中几个固定位置提取出特定的数据字段
（比如文件或类似格式）：

"""
###### 0123456789012345678901234567890123456789012345678901234567890'
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print(cost)
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)
