#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
你有一些长字符串，想以指定的列宽将它们重新格式化。
解决方案
使用 textwrap 模块来格式化字符串的输出。比如，假如你有下列的长字符串：
"""
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
import textwrap

text = textwrap.fill(s, 40)
print(text)
# 首行缩进
text = textwrap.fill(s, 40, initial_indent='    ')
print(text)
text = textwrap.fill(s, 40, subsequent_indent='    ')
print(text)

