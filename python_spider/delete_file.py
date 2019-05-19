#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import random
import time

print('\xa3')


def remove_file(path):
    try:
        os.remove(path)
        print('file: %s delete success!' % path)
    except Exception as e:
        print(str(e))


def main():
    file_path = r'C:\Users\liming\Desktop\program\python_spider'
    for path, dirs, files in os.walk(file_path):
        for file in files:
            if file.endswith('.mp4'):
                remove_file(os.path.sep.join([path, file]))


if __name__ == '__main__':
    main()
