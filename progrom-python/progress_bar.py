#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
from tqdm import tqdm

for i in tqdm(range(1000)):
    sleep(0.01)
# print('ok')
text = ""
for char in tqdm(["a", "b", "c", "d"]):
    sleep(0.1)
    text = text + char
    print(text)
