#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
你想匹配或者搜索特定模式的文本
解决方案
如果你想匹配的是字面字符串，那么你通常只需要调用基本字符串方法就行，比如
str.find() , str.endswith() , str.startswith() 或者类似的方法：
"""
text = 'yeah, but no, but yeah, but no, but yeah'
print(text=='yeah')
print(text.startswith('yeah'))
print(text.endswith('no'))
print(text.find('no'))

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re

if re.match(r'\d+/\d+/\d+',text2):
    print('yes')
else:
    print('no')

datepat=re.compile(r'(\d+)/(\d+)/(\d+)')
if datepat.match(text1):
    print('yes')
else:
    print('no')
text='Today is 11/27/2012. PyCon starts 3/13/2013.'
dates=datepat.findall(text)
print(dates)
for mon,day,year in dates:
    print('{}--{}--{}'.format(year,mon,day))

for m in datepat.finditer(text):
    print(m.groups())
