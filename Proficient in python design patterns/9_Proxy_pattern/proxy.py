#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class SensitiveInfo:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    def read(self):
        print('There are {} users: {}'.format(len(self.users), ' '.join(self.users)))

    @abstractmethod
    def add(self, user):
        self.users.append(user)
        print('Add user {}'.format(user))

    @abstractmethod
    def remove(self, user):
        self.users.remove(user)
        print('Remove user {}'.format(user))


class Info:
    '''SensitiveInfo的保护代理'''

    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = '0xdeadbeef'

    def read(self):
        self.protected.read()

    def add(self, user):
        sec = input('what is the secret? ')
        self.protected.add(user) if sec == self.secret else print("That's wrong!")

    def remove(self, user):
        sec = input('what is the secret? ')
        if sec != self.secret:
            return "That's wrong!"
        if not user in self.protected.users:
            return "That's user not exist!"
        self.protected.remove(user) if sec == self.secret else print("That's wrong!")


def main():
    info = Info()
    while True:
        print('1. read list |==| 2. add user |==| 3. remove |==| 4. quit')
        key = input('choose option: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username: ')
            info.add(name)
        elif key == '3':
            name = input('choose username: ')
            info.remove(name)
        elif key == '4':
            exit()
        else:
            print('unknown option: {}'.format(key))


if __name__ == '__main__':
    main()
