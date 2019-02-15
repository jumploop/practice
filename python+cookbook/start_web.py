#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
你想通过脚本启动浏览器并打开指定的 URL 网页
解决方案
webbrowser 模块能被用来启动一个浏览器，并且与平台无关。例如：
"""
import webbrowser


def open_web(url):
    ret = webbrowser.open(url)
    return ret


if __name__ == '__main__':
    url = 'http://www.python.org'
    open_web(url)
