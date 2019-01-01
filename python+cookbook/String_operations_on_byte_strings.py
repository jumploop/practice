#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
你想在字节字符串上执行普通的文本操作 (比如移除，搜索和替换)。
解决方案
字节字符串同样也支持大部分和文本字符串一样的内置操作。比如：
"""

data = b'Hello World'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))
data = bytearray(b'Hello World')
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))
data = b'FOO:BAR,SPAM'
import re

ret = re.split(b'[:,]', data)  # Notice: pattern as bytes
print(ret)
print('{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii'))