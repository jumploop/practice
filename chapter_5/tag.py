def tag(name, *content, cls=None, **attrs):
    """生成一个或多个HTML标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


ret = tag('br')
print(ret)
ret = tag('p', 'hello')
print(ret)
print(tag('p', 'hello', 'world'))
ret = tag('p', 'hello', id=33)
print(ret)
print(tag('p', 'hello', 'world', cls='sidebar'))
ret = tag(content='testing', name="img")
print(ret)

my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
ret=tag(**my_tag)
print(ret)
