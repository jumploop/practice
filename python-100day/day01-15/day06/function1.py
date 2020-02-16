#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
函数的定义和使用 - 计算组合数C(7,3)

"""


# 将求阶乘的功能封装成一个函数
def factorial(n):
    """
    求阶乘
    :param n: 非负整数
    :return: num的阶乘
    """
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result


print(factorial(7) // factorial(3) // factorial(4))


