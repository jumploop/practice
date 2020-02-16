# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
用while循环实现1~100之间的偶数求和

"""
sum = 0
num = 2
while num <= 100:
    sum += num
    num += 2
print(sum)
