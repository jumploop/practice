#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...

"""

a=0
b=1
for _ in range(20):
    (a,b)=(b,a+b)
    print(a,end=" ")
