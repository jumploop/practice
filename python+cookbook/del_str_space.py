#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
你想去掉文本字符串开头，结尾或者中间不想要的字符，比如空白。
解决方案
strip() 方法能用于删除开始或结尾的字符。 lstrip() 和 rstrip() 分别从左和
从右执行删除操作。默认情况下，这些方法会去除空白字符，但是你也可以指定其他字符。比如：
"""
# Whitespace stripping
s = ' hello world \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())
t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))
filename='somefile.txt'
with open(filename)as f:
   lines=(line.strip() for line in f)
   # print(lines)
   for line in lines:
       print(line)