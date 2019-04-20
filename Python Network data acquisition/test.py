#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
nameList = bsObj.findAll("span", {"class": "green"})
for name in nameList:
    print(name.get_text())
nameList = bsObj.findAll('span', {'class': {'green', 'red'}})
print(len(nameList))
nameList = bsObj.findAll(text='the prince')
print(len(nameList))

allText = bsObj.findAll(id="text")
print(allText[0].get_text())
