#!/usr/bin/env python
# -*- coding: utf-8 -*-

def to_str(bytes_or_str):
    """
    接受str或bytes，返回str
    :param bytes_or_str:
    :return:
    """
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # instance of str


def to_bytes(bytes_or_str):
    """
    接受str或bytes，返回bytes
    :param bytes_or_str:
    :return:
    """
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # instance of bytes

def main():
    msg=input()
    value=to_bytes(msg)
    print(value)
    value=to_str(value)
    print(value)

if __name__ == '__main__':
    main()