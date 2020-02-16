#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pip
from subprocess import call,Popen,PIPE,STDOUT

from pip._internal.utils.misc import get_installed_distributions
pip_list=[]
p=Popen('pip  list --outdated',stdout=PIPE,stderr=PIPE,shell=True)
for line in p.stdout.readlines():
    new_line=line.decode('utf-8')
    print(new_line)
    pip_list.append(new_line.split()[0])
    call("pip install --upgrade " + new_line.split()[0], shell=True)
print(pip_list)

# for dist in get_installed_distributions():
#     call("pip install --upgrade " + dist.project_name, shell=True)
