#!/usr/bin/env python
# -*- coding: utf-8 -*-
MINI14 = '1.4GHz Mac mini'


class AppleFactory(object):
    class MacMini14(object):
        def __init__(self):
            self.memory = 4  # 单位GB
            self.hdd = 500  # 单位GB
            self.gpu = 'Intel HD Graphics 5000'

        def __str__(self):
            info = ('Model: {}'.format(MINI14),
                    'Memory: {}GB'.format(self.memory),
                    'Hard Disk: {}GB'.format(self.hdd),
                    'Graphics Card: {}'.format(self.gpu))
            return '\n'.join(info)

    def build_computer(self, model):
        if (model == MINI14):
            return self.MacMini14()
        else:
            print("I dont't know how to build {}".format(model))


if __name__ == '__main__':
    afac = AppleFactory()
    mac_mini = afac.build_computer(MINI14)
    print(mac_mini)