#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
怎样找出一个序列中出现次数最多的元素呢？
解决方案
collections.Counter 类就是专门为这类问题而设计的，它甚至有一个有用的
most_common() 方法直接给了你答案。
为了演示，先假设你有一个单词列表并且想找出哪个单词出现频率最高。你可以这
样做：
"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
# print(word_counts)
# 出现频率最高的3个单词
top_three = word_counts.most_common(3)
# print(top_three)
# 在底层实现上，一个 Counter 对象就是一个字典，将元素映射到它出现的次数上
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1
# print(word_counts['eyes'])
a=Counter(words)
b=Counter(morewords)
print(a,'\n\r',b)
c=a+b
print(c)
d=a-b
print(d)
