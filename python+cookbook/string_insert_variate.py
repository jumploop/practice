#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
你想创建一个内嵌变量的字符串，变量被它的值所表示的字符串替换掉。
解决方案
Python 并没有对在字符串中简单替换变量值提供直接的支持。但是通过使用字符
串的 format() 方法来解决这个问题。比如：
"""
s = '{name} has {n} messages.'
new_s = s.format(name='Guido', n=37)
print(new_s)
name = 'Guido'

n = 37


# ret = s.format_map(vars())


# print(ret)

class Info(object):
    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info('Guido', 37)
ret2 = s.format_map(vars(a))


# print(ret2)

class safesub(dict):
    """ 防止 key 找不到"""

    def __missing__(self, key):
        return '{' + key + '}'


ret3 = s.format_map(safesub(vars()))
print(ret3)
import sys


def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))


print(sub('Hello {name}'))
print(sub('You have {n} messages.'))

print(sub('Your favorite color is {color}'))
# print('%(name) has %(n) messages.' % vars())
import string

s = string.Template('$name has $n messages.')
print(s.substitute(vars()))
