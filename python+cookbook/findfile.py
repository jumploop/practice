#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys


def findfile(start,name):
    for relpath,dirs,files in os.walk(start):
        if name in files:
            full_path=os.path.join(start,relpath,name)
            print(os.path.normpath(os.path.abspath(full_path)))

if __name__ == '__main__':
    start=sys.argv[1]
    name=sys.argv[2]
    findfile(start,name)