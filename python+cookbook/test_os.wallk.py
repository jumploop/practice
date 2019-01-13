#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

for path,dirs,files in os.walk(r'C:\Users'):
    for file in files:
        print(os.path.join(path,file))