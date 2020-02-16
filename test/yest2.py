#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import threading
from multiprocessing import Process

import cchardet
import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('used:', end - start)
        return result

    return wrapper


@timeit
def get_encoding(file):
    with open(file, 'rb')as f:
        data = f.read()
        encode = cchardet.detect(data)['encoding']
        return encode


@timeit
def get_files(file_path):
    for root, dirs, files in os.walk(file_path):
        for file in files:
            full_path = os.path.join(root, file)
            encode = get_encoding(full_path)
            print(file, "-->", encode)


@timeit
def foo():
    for i in range(10000):
        pass


def func(x):
    print(x)




if __name__ == '__main__':
    get_files(".")
    foo()
    # t = threading.Thread(target=func, args=(12,))
    # # 线程启动
    # t.start()
    # # 主进程阻塞，等待子进程的退出
    # t.join()
    # 设置线程为主线程的守护线程
    p = Process(target=func, args=(12,))
    p.daemon = True

    p.start()  # 启动子进程实例(创建子进程)
    p.is_alive()  # 判断进程子进程是否还在活着

    p.join()  # 是否等待子进程执行结束，或者等待多少秒
    p.terminate()  # 不管任务是否完成，立即终止子进程
    # p.daemon = True  # 设置守护进程