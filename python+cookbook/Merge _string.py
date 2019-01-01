#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
你想将几个小的字符串合并为一个大的字符串
解决方案
如果你想要合并的字符串是在一个序列或者 iterable 中，那么最快的方式就是使
用 join() 方法。比如：
"""
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
new_str = ' '.join(parts)
print(new_str)
data = ['ACME', 50, 91.1]
ret = ','.join(str(s) for s in data)
print(ret)
a = 'Is Chicago'
b = 'Not Chicago?'
c = 'hello world!'
print(a,b,c,sep=':')
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

text=''.join(sample())
print(text)
with open('test.txt','a')as f:
    for part in sample():
        f.write(part)

def combine(source, maxsize):
    parts=[]
    size=0
    for part in source:
        parts.append(part)
        size+=len(part)
        if size >maxsize:
            yield ''.join(parts)
            parts=[]
            size=0
        yield ''.join(parts)
# 结合文件操作
with open('filename', 'w') as f:
    for part in combine(sample(), 32768):
        f.write(part)