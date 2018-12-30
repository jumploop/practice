#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
你需要通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀， URL
Scheme 等等。
解决方案
检查字符串开头或结尾的一个简单方法是使用 str.startswith() 或者是 str.
endswith() 方法。比如
"""
from pprint import pprint

filename = 'spam.txt'
# endswith()返回布尔值
ret = filename.endswith('.txt')
# print(ret)
url = 'http://www.python.org'
ret2 = url.startswith('http:')
# print(ret2)
# 如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去，然后传
# 给 startswith() 或者 endswith() 方法
import os


def check_file():
    """
    检查文件名字
    :return:
    """
    filenames = os.listdir('.')
    # print(filenames)
    name = [name for name in filenames if name.endswith(('.py', '.txt'))]
    # print(name)
    return name


from urllib.request import urlopen
import requests

def read_data(name):
    if name.startswith(('http:', 'ftp:', 'https:')):
        # return urlopen(name).read()
        return requests.get(name).content.decode('utf-8')
    else:
        with open(name) as f:
            return f.read()


if __name__ == '__main__':
    ret = check_file()
    pprint(ret)
    msg=read_data('http://www.python.org')
    print(msg)
