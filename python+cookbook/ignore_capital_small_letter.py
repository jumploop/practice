#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
你需要以忽略大小写的方式搜索与替换文本字符串
解决方案
为了在文本操作时忽略大小写，你需要在使用 re 模块的时候给这些操作提供
re.IGNORECASE 标志参数。比如：
"""
import re


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace


text = 'UPPER PYTHON, lower python, Mixed Python'
ret = re.findall('python', text, flags=re.I)
print(ret)
ret2 = re.sub('python', matchcase('snake'), text, flags=re.I)
print(ret2)
