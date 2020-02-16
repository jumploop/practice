#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
用for循环实现1~100的偶数求和
"""

sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum += i
print(sum)
