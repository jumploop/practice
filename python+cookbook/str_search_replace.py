#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
你想在字符串中搜索和匹配指定的文本模式解决方案
对于简单的字面模式，直接使用 str.replace() 方法即可，比如：
"""
import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
text2 = 'yeah, but no, but yeah, but no, but yeah'
new_text = text2.replace('yeah', 'yep')
print(new_text)
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
ret = datepat.sub(r'\3-\1-\2', text)
print(ret)

from calendar import month_abbr


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


date = datepat.sub(change_date, text)
print(date)
