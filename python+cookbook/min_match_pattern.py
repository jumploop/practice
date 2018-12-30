#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
你正在试着用正则表达式匹配某个文本模式，但是它找到的是模式的最长可能匹
配。而你想修改它变成查找最短的可能匹配。
解决方案
这个问题一般出现在需要匹配一对分隔符之间的文本的时候 (比如引号包含的字符
串)。为了说明清楚，考虑如下的例子：
"""
import re

str_pat = re.compile(r'\"(.*?)\"')
text1 = 'Computer says "no."'
ret=str_pat.findall(text1)
print(ret)
text2 = 'Computer says "no." Phone says "yes."'
ret2=str_pat.findall(text2)
print(ret2)