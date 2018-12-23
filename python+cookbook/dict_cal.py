#!/usr/bin/env python
# -*- coding: utf-8 -*-
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.76
}
min_price=min(zip(prices.values(),prices.keys()))
print(min_price)
# print(prices.values())
# print(prices.keys())
max_price=max(zip(prices.values(),prices.keys()))
print(max_price)
prices_sorted=sorted(zip(prices.values(),prices.keys()))
print(prices_sorted)
# print(prices_sorted)