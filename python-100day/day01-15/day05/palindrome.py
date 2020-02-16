#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
判断输入的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数
"""
number = int(input("请输入一个正整数："))
temp = number
number2 = 0
while temp > 0:
    number2 *= 10
    number2 += temp % 10
    temp //= 10
if number2 == number:
    print("%d是回文数" % number)
else:
    print("%d不是回文数" % number)
