#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from collections import OrderedDict

d = OrderedDict()

d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    # time.sleep(1)
    print(key, d[key],flush=True)
#