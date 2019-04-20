#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.error import HTTPError

from bs4 import BeautifulSoup

from urllib.request import urlopen


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


def main():
    title = getTitle("http://www.pythonscraping.com/pages/page1.html")
    if title is None:
        print('title could not found!')
    else:
        print('title:',title)


if __name__ == '__main__':
    main()
