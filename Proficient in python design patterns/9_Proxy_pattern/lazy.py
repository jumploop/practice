#!/usr/bin/env python
# -*- coding: utf-8 -*-

class LazyProperty:
    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__

    def __get__(self, obj, cls):
        if not obj:
            return None
        value = self.method(obj)
        setattr(obj, self.method_name, value)
        return value


class Test:
    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None

    @LazyProperty
    def resource(self):
        print('initializing self._resource which is: {}'.format(self._resource))
        self._resource = tuple(range(5))  # 假设这一行的计算成本比较大
        return self._resource


def main():
    t = Test()
    print(t.x)
    print(t.y)
    # 做更多的事情……
    print(t.resource)
    print(t.resource)


if __name__ == '__main__':
    main()
