#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import pymysql


# 1.0连接数据库

class DBReport:
    def __init__(self):
        self._conn = None
        self._connect()
        self._cursor = self._conn.cursor()

    def _connect(self):
        '''连接数据库'''
        try:
            self._conn = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                passwd='mysql',
                db='data',
                charset='utf8')
        except Exception as e:
            print(str(e))

    def query(self, sql):
        try:
            result = self._cursor.execute(sql)
        except Exception as e:
            print(e)
            result = False
        return result

    def select(self, table, column='*', condition=''):
        condition = ' where ' + condition if condition else None
        if condition:
            sql = "select %s from %s %s" % (column, table, condition)
        else:
            sql = "select %s from %s" % (column, table)
        self.query(sql)
        return self._cursor.fetchall()

    def insert(self, table, tdict):
        column = ''
        value = ''
        for key in tdict:
            column += ',' + key
            value += "','" + tdict[key]
        column = column[1:]
        value = value[2:] + "'"
        sql = "insert into %s(%s) values(%s)" % (table, column, value)
        self._cursor.execute(sql)
        self._conn.commit()
        return self._cursor.lastrowid  # 返回最后的id

    def update(self, table, tdict, condition=''):
        if not condition:
            print("must have id")
            exit()
        else:
            condition = 'where ' + condition
        value = ''
        for key in tdict:
            value += ",%s='%s'" % (key, tdict[key])
        value = value[1:]
        sql = "update %s set %s %s" % (table, value, condition)
        self._cursor.execute(sql)
        return self.affected_num()  # 返回受影响行数

    def delete(self, table, condition=''):
        condition = 'where ' + condition if condition else None
        sql = "delete from %s %s" % (table, condition)
        # print sql
        self._cursor.execute(sql)
        self._conn.commit()
        return self.affected_num()  # 返回受影响行数

    def rollback(self):
        self._conn.rollback()

    def affected_num(self):
        return self._cursor.rowcount

    def __del__(self):
        try:
            self._cursor.close()
            self._conn.close()
        except:
            pass

    def close(self):
        self.__del__()

    # 2.0添加数据表
    # 开始时间,来访ID,二级分类,三级分类,四级分类,五级分类,备注,服务方式,TIME_LOAD
    def create_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS DATA (
            ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            开始时间 CHAR(60),
            来访ID CHAR(30),
            二级分类 CHAR(30),
            三级分类 CHAR(30),
            备注 TEXT(2000),
            TIME_LOAD CHAR(60)
            );
            """
        self._cursor.execute(sql)
        print('正在创建数据表')

    def insert_data(self):
        time_load = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sql = 'insert into data (开始时间,来访ID,二级分类,三级分类,备注,TIME_LOAD) values (%s, %s, %s, %s, %s, %s)'
        try:
            print('写入数据库....')
            self._cursor.execute(sql, ('20190506', '120', '技术', '程序员', 'hello', time_load))
            self._conn.commit()
            print('写入数据成功')
        except Exception as e:
            print(str(e))


def main():
    db = DBReport()
    db.create_table()
    db.insert_data()
    db.close()


if __name__ == '__main__':
    main()
