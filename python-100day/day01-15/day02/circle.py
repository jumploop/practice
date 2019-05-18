#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
输入半径计算圆的周长和面积
"""
import math

radius = float(input('请输入圆的半径：'))
# 周长
perimeter = 2 * math.pi * radius
print('圆的周长：%.2f' % perimeter)
# 面积
area = math.pi * radius ** 2
print('圆的面积：%.2f' % area)
