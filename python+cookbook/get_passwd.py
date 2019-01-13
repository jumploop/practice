#!/usr/bin/env python
# -*- coding: utf-8 -*-
import getpass

user=input('Enter your username:')
passwd=input()


def svc_login(user, passwd):
    if user=='root'and passwd=='123':
        return True


if svc_login(user, passwd): # You must write svc_login()
    print('Yay!')
else:
    print('Boo!')