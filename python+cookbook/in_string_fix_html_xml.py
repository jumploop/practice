#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
你想将 HTML 或者 XML 实体如 &entity; 或 &#code; 替换为对应的文本。再者，
你需要转换文本中特定的字符 (比如 <, >, 或 &)。
解决方案
如果你想替换文本字符串中的‘<’或者‘>’，使用 html.escape() 函数可以很
容易的完成。比如：
"""
s = 'Elements are written as "<tag>text</tag>".'
import html

print(s)
print(html.escape(s))
# Disable escaping of quotes
print(html.escape(s, quote=False))
# 如果你正在处理的是 ASCII 文本，并且想将非 ASCII 文本对应的编码实体嵌入进
# 去，可以给某些 I/O 函数传递参数 errors='xmlcharrefreplace' 来达到这个目。比
# 如：
s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))

# 为了替换文本中的编码实体，你需要使用另外一种方法。如果你正在处理 HTML
# 或者 XML 文本，试着先使用一个合适的 HTML 或者 XML 解析器。通常情况下，这
# 些工具会自动替换这些编码值，你无需担心。
# 有时候，如果你接收到了一些含有编码值的原始文本，需要手动去做替换，通常你
# 只需要使用 HTML 或者 XML 解析器的一些相关工具函数/方法即可。比如：
s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser

p = HTMLParser()
print(p.unescape(s))
# The unescape method is deprecated and will be removed in 3.5, use html.unescape() instead. more... (Ctrl+F1)
print(html.unescape(s))
t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))