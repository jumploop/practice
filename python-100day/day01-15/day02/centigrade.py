#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
将华氏温度转换为摄氏温度
F = 1.8C + 32
"""
f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8
print(c)
print('%.1f华氏度=%.1f摄氏度' % (f, c))
