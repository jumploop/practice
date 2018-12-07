import html

def htmlize(obj):
    content=html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

ret=htmlize(({1,2,3}))
print(ret)