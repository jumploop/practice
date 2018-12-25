#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
你有一个字典或者实例的序列，然后你想根据某个特定的字段比如 date 来分组迭
代访问。
解决方案
itertools.groupby() 函数对于这样的数据分组操作非常实用。为了演示，假设你
已经有了下列的字典列表：
"""
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
from operator import attrgetter, itemgetter
from itertools import groupby

# Sort by the desired field first
rows.sort(key=itemgetter('date'))
# Iterate in group
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)
from collections import defaultdict

rows_by_date = defaultdict(list)
for row in rows:
   rows_by_date[row['date']].append(row)
   # print(row)
# print(rows_by_date)
for r in rows_by_date['07/01/2012']:
    print(r)