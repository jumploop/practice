#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
你正在处理 Unicode 字符串，需要确保所有字符串在底层有相同的表示。
解决方案
在 Unicode 中，某些字符能够用多个合法的编码表示。为了说明，考虑下面的这个
例子：
"""

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
# print(s1)
# print(s2)
# print(len(s1))
# print(len(s2))
import unicodedata
t1=unicodedata.normalize('NFC',s1)
t2=unicodedata.normalize('NFC',s2)
print(t1)
print(t2)
print(t1==t2)
print(ascii(t1))
t3=unicodedata.normalize('NFD',s1)
t4=unicodedata.normalize('NFD',s2)
print(t3)
print(t4)
print(ascii(t3))
strs=''.join(c for c in t3 if not unicodedata.combining(c))
print(strs)