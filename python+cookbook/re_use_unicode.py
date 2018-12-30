#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
你正在使用正则表达式处理文本，但是关注的是 Unicode 字符处理。
解决方案
默认情况下 re 模块已经对一些 Unicode 字符类有了基本的支持。比如， \\d 已经
匹配任意的 unicode 数字字符了：
"""
import re

num=re.compile(r'\d+')
print(num.match('123').group())
print(num.match('\u0661\u0662\u0663').group())
pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
ret=pat.match(s) # Matches
print(ret.group())
print(s.upper())