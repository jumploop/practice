#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os


def shutdown_computer():
    runing = True
    while runing:
        inputs = input("关机(s)OR重启(r)?(q退出)")
        inputs = inputs.lower()
        if inputs == 'q' or inputs == 'quit':
            runing = False
            print("程序退出")
            break
        elif inputs == 's':
            seconds = int(input("请输入暂停时间(单位:秒):"))
            #    a =input("sleep time:")
            print("暂停时间:", seconds)
            runing = False
            time.sleep(seconds)
            print("关机ing")
            os.system("shutdown -s -t  60 ")
        elif inputs == 'r':
            print("重启ing")
            os.system('reboot')
        else:
            print("程序错误重新输入")
            runing = True
        print("程序结束~~~!")


def main():
    shutdown_computer()


if __name__ == '__main__':
    main()
