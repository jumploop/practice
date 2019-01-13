#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput

# with fileinput.input()as f_input:
#     for line in f_input:
#         print(line,end='')

with fileinput.input('somefile.txt')as f:
    for line in f:
        print(f.filename(),f.lineno(),line,end='')