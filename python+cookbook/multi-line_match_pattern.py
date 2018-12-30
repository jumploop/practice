#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
你正在试着使用正则表达式去匹配一大块的文本，而你需要跨越多行去匹配。
解决方案
这个问题很典型的出现在当你用点 (.) 去匹配任意字符的时候，忘记了点 (.) 不能
匹配换行符的事实。比如，假设你想试着去匹配 C 语言分割的注释：
"""
import re

comment = re.compile(r'/\*(.*?)\*/',re.S)
text1 = '/* this is a comment */'
text2 = '''/* this is a
... multiline comment */
... '''

result = comment.findall(text1)
print(result)
result2 = comment.findall(text2)
print(result2)
comment2 = re.compile(r'/\*((?:.|\n)*?)\*/')
msg=comment2.findall(text2)
print(msg)