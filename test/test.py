import re

# p = re.compile(r'\d+')
# for m in p.finditer('one1two2three3four4'):
#     print (m.group())

import builtins
from collections import ChainMap

pylookup = ChainMap(locals(), globals(), vars(builtins))
print(pylookup)