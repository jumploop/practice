#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
输出乘法口诀表(九九表)

"""
for x in range(1,10):
    for y in range(1,x+1):
        print("%d*%d=%d"%(x,y,x*y),end="\t")
    print()
