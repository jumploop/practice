#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess

p = subprocess.Popen('python', shell=False)
if not p.poll() is None:
    p.wait()
print(p)
# print(p.wait())

