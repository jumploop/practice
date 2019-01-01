#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
你有一个字符串，想从左至右将其解析为一个令牌流。
解决方案
假如你有下面这样一个文本字符串：
"""
from collections import namedtuple

text = 'foo = 23 + 42 * 10'
# 为了令牌化字符串，你不仅需要匹配模式，还得指定模式的类型。比如，你可能想
# 将字符串像下面这样转换为序列对：
tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'),
          ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
import re

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
scanner = master_pat.scanner('foo = 42')
_ = scanner.match()
print(scanner.match())
print(_.lastgroup, _.group())


def generate_tokens(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


# Example use
for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)

# Produces output
# Token(type='NAME', value='foo')
# Token(type='WS', value=' ')
# Token(type='EQ', value='=')
# Token(type='WS', value=' ')
# Token(type='NUM', value='42')
print("*" * 50)
# 如果你想过滤令牌流，你可以定义更多的生成器函数或者使用一个生成器表达式。
# 比如，下面演示怎样过滤所有的空白令牌：
tokens = (tok for tok in generate_tokens(master_pat, text)
          if tok.type != 'WS')
for tok in tokens:
    print(tok)

# 令牌的顺序也是有影响的。 re 模块会按照指定好的顺序去做匹配。因此，如果一
# 个模式恰好是另一个更长模式的子字符串，那么你需要确定长模式写在前面。比如：
LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'
master_pat = re.compile('|'.join([LE, LT, EQ]))  # Correct
# master_pat = re.compile('|'.join([LT, LE, EQ])) # Incorrect

# 第二个模式是错的，因为它会将文本 <= 匹配为令牌 LT 紧跟着 EQ，而不是单独
# 的令牌 LE，这个并不是我们想要的结果。
# 最后，你需要留意下子字符串形式的模式。比如，假设你有如下两个模式：
print('*'*50)
PRINT = r'(?P<PRINT>print)'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
master_pat2 = re.compile('|'.join([PRINT, NAME]))
for tok in generate_tokens(master_pat2, 'printer'):
    print(tok)
# Outputs :
# Token(type='PRINT', value='print')
# Token(type='NAME', value='er')
