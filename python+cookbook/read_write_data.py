#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 问题
# 你需要读写各种不同编码的文本数据，比如 ASCII， UTF-8 或 UTF-16 编码等。
# 解决方案
# 使用带有 rt 模式的 open() 函数读取文本文件。如下所示：
# Read the entire file as a single string
with open('somefile.txt', 'rt') as f:
    data = f.read()
    print(data)
# Iterate over the lines of the file
with open('somefile.txt', 'rt') as f:
    for line in f:
        print(line)
with open('test.txt', 'wt')as f:
    print('hello world!', file=f)
print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=',', end='!!\n')
for i in range(5):
    print(i, end='')
print()
row = ('ACME', 50, 91.5)
print(*row, sep=',')

with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    print(data)
    text = data.decode('utf-8')
    print(text)

with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))
import array

nums = array.array('i', [1, 2, 3, 4])
# print(nums)
with open('data.bin', 'wb')as f:
    f.write(nums)
a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('data.bin', 'rb')as f:
    print(f.readinto(a))

with open('anyfile', 'wt')as f:
    f.write('hello\n')

# with open('anyfile','xt')as f:
#     f.write('hello\n')
from functools import partial

RECORD_SIZE = 32
with open('somefile.data', 'rb')as f:
    # f.write(b'hello\n')
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)

import os.path


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf


with open('sample.bin', 'wb') as f:
    f.write(b'hello world!')
buf = read_into_buffer('sample.bin')
print(buf)
print(buf[0:5])
with open('newsample.bin', 'wb')as f:
    r = f.write(buf)
    print(r)

record_size = 32  # Size of each record (adjust value)
buf = bytearray(record_size)
with open('somefile', 'rb') as f:
    while True:
        n = f.readinto(buf)
        if n < record_size:
            break
print(buf)
m1=memoryview(buf)
print(m1)
m2=m1[-5:]
print(m2)
m2[:]=b'WPRLD'
print(buf)