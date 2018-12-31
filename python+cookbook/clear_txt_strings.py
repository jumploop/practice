#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
问题
一些无聊的幼稚黑客在你的网站页面表单中输入文本” pýtĥöñ”，然后你想将这些
字符清理掉。
解决方案
文本清理问题会涉及到包括文本解析与数据处理等一系列问题。在非常简单的情
形下，你可能会选择使用字符串函数 (比如 str.upper() 和 str.lower() ) 将文本转为
标准格式。使用 str.replace() 或者 re.sub() 的简单替换操作能删除或者改变指定
的字符序列。你同样还可以使用 2.9 小节的 unicodedata.normalize() 函数将 unicode
文本标准化。
然后，有时候你可能还想在清理操作上更进一步。比如，你可能想消除整个区间上
的字符或者去除变音符。为了这样做，你可以使用经常会被忽视的 str.translate()
方法。为了演示，假设你现在有下面这个凌乱的字符串：
"""
s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None
}
a = s.translate(remap)
print(a)
import unicodedata
import sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chrs))
digitmap = {c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode)
            if unicodedata.category(chr(c)) == 'Nd'}
print(len(digitmap))
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))
result = b.encode('ascii', 'ignore').decode('ascii')
print(result)


def clean_spaces(s):
    """
    清理空白字符
    :param s:
    :return:
    """
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s
