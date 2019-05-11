#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import urllib
import pymysql
import time
import platform

import requests


def log_w(text):
    logfile = "websocket.log"
    if os.path.isfile(logfile):
        if (os.path.getsize(logfile) / 1024 / 1024) > 100:
            os.remove(logfile)
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    tt = str(now) + "\t" + str(text) + "\n"
    f = open(logfile, 'a+')
    f.write(tt)
    f.close()


def get_idcname(ip):
    try:
        conn = pymysql.connect(host='192.168.8.43', port=3306, user='read_app', passwd='123456', charset='utf8')
        cursor = conn.cursor()
        # 查询出的结果是元组形式，元组和列表基本一样
        # cursor = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)#查询结果是字典形式
        sql = "select host,user from mysql.user where host='%s'" % ip
        # python中执行sql语句一次只能是一个sql语句，一次只执行
        cursor.execute(sql)
        # 执行sql语句
        # cursor.executemany("""insert into dist_sniffer.sniffer_order_day values(%s,%s,%s,%s,%s,%s,%s,%s,%s) """,value
        alldata = cursor.fetchall()
        # 接收sql执行结果，如果是写操作的，这个就不用了
        # conn.commit()如果是写操作，需要这个去提交
        cursor.close()
        conn.close()  # 关闭数据库回话
        return alldata[0][0].encode('UTF8')  # 如果是写操作的话就没有返回值了。
    except Exception as e:
        return 0


def get_ip():
    os = platform.system()
    if os == "Linux":
        ip = os.popen("/sbin/ifconfig eth0|grep 'inet addr'").read().strip().split(":")[1].split()[0]
    elif os == "Windows":
        import wmi
        c = wmi.WMI()
        network = c.Win32_NetworkAdapterConfiguration(IPEnabled=1)
        print(network)
        for interface in network:
            if interface.DefaultIPGateway:
                ip = interface.IPAddress[0]
                print(ip)
                return ip
            # print interface.IPAddress[0],interface.MACAddress,interface.IPSubnet[0],interface.DefaultIPGateway[0],interfa
            # 获取出网的ip地址、MAC地址、子网掩码、默认网关、DNS
def web_status():
    ip = get_ip()
    idc_name = get_idcname(ip)
    url = "http://www.text.com/index.php?idc_ip=%s&idc_name=%s" % (ip, idc_name)
    get = urllib.request.urlopen(url)
    print(get.read())
    if get.getcode == 200:
        aa = int(get.read().strip())
        print(aa)
        if aa == 1:
            text = "Webservice return OK"
        else:
            text = "Webservice return Error"
    else:
        text = "Conect webservice Error"
    print(text)
    log_w(text)


if __name__ == "__main__":
    web_status()
