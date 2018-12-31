#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
你想通过某种对齐方式来格式化字符串
解决方案
对于基本的字符串对齐操作，可以使用字符串的 ljust() , rjust() 和 center()
方法。比如：
"""
text = 'Hello World'
print(text.ljust(20,'='))
print(text.rjust(20,'+'))
print(text.center(20,'-'))
print(format(text, '=>20s'))
print(format(text, '-<20s'))
print(format(text, '*^20s'))
print('{:>10s} {:>10s}'.format('Hello', 'World'))
x = 1.2345
print(format(x,'>20'))
print(format(x,'^10.2f'))