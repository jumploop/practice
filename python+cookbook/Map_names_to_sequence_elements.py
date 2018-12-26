#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
你有一段通过下标访问列表或者元组中元素的代码，但是这样有时候会使得你的
代码难以阅读，于是你想通过名称来访问元素。
解决方案
collections.namedtuple() 函数通过使用一个普通的元组对象来帮你解决这个问
题。这个函数实际上是一个返回 Python 中标准元组类型子类的一个工厂方法。你需要
传递一个类型名和你需要的字段给它，然后它就会返回一个类，你可以初始化这个类，
为你定义的字段传递值等。代码示例：
"""
from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)
print(len(sub))
addr, joined = sub
print(addr)
print(joined)


def computer_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


stock_prototype = Stock('', 0, 0.0, None, None)


# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)


if __name__ == '__main__':
    # s = Stock('ACME', 100, 123.45)
    # s_list = [s]
    # ret = compute_cost(s_list)
    # print(ret)
    # Create a prototype instance
    a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
    ret = dict_to_stock(a)
    print(ret)
    b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
    ret = dict_to_stock(b)
    print(ret)
