#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
函数的定义和使用 - 求最大公约数和最小公倍数

"""


def gcd(x, y):
    """
    计算最大公约数
    :param x: 数字x
    :param y: 数字y
    :return: 最大公约数
    """
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 1, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
    return 1


def lcm(x, y):
    """
    计算最小公倍数
    :param x: 数字x
    :param y: 数字y
    :return: 最小公倍数
    """
    return x * y // gcd(x, y)


print(gcd(3, 6))
print(lcm(3, 6))
