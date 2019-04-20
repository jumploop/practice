#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# def fibonacci(n):
#     assert (n >= 0), 'n must be >= 0'
#
#     return n if n in (0, 1) else fibonacci(n - 1) + fibonacci(n - 2)


known = {0: 0, 1: 1}


def fibonacci(n):
    assert (n >= 0), 'n must be >= 0'
    if n in known:
        return known[n]
    res = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = res
    return res


known_sum = {0: 0}


def nsum(n):
    assert (n >= 0), 'n must be >= 0'
    if n in known_sum:
        return known_sum[n]
    res = n + nsum(n - 1)
    known_sum[n] = res
    return res


if __name__ == '__main__':
    ret = fibonacci(8)
    print(ret)
    from timeit import Timer

    t = Timer('fibonacci(100)', 'from __main__ import fibonacci')
    print(t.timeit())
