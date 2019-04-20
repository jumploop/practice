#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cowpy import cow


def dots_style(msg):
    '''简单地将msg首字母大写，并在其之前和之后输出10个点。'''
    msg = msg.capitalize()
    msg = '.' * 10 + msg + '.' * 10
    return msg


def admire_style(msg):
    msg = msg.upper()
    return '!'.join(msg)


def cow_style(msg):
    msg = cow.milk_random_cow(msg)
    return msg


def generate_banner(msg, style=dots_style):
    '''横幅生成器'''
    print('-- start of banner --')
    print(style(msg))
    print('-- end of banner --\n\n')


def main():
    msg = 'happy coding'
    [generate_banner(msg, style) for style in (dots_style, admire_style, cow_style)]


if __name__ == '__main__':
    main()
