#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

import pymysql
import requests
from bs4 import BeautifulSoup
import urllib.request


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
                db='fast_track',
                charset='utf8')
        except Exception as e:
            print(str(e))

    def create_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS `Tech_Track_100`(
                `id` INT NOT NULL AUTO_INCREMENT,
                `Rank` INT,
                `CompanyName` VARCHAR(60),
                `Webpage` VARCHAR(60),
                `Description` VARCHAR(60),
                `Location` VARCHAR(30),
                `Yearend` TEXT(2000),
                `Annual sales rise over 3 years` VARCHAR(60),
                `Sales` VARCHAR (30),
                `Staff` VARCHAR (30),
                `Comments` TEXT(2000),
                PRIMARY KEY ( `id` )     
                )ENGINE=InnoDB DEFAULT CHARSET=utf8;
               '''
        self._cursor.execute(sql)
        print('正在创建数据表')

    def insert_data(self, data):
        sql = '''INSERT INTO Tech_Track_100(
                `Rank`,`CompanyName`,`Webpage`,`Description`,`Location`,`Yearend`,`Annual sales rise over 3 years`,`Sales`,`Staff`,`Comments`) 
                VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s, %s);'''
        try:
            print('写入数据库....')
            self._cursor.execute(sql, data)
            self._conn.commit()
            print('写入数据成功')
        except Exception as e:
            print(str(e))
            self.rollback()

    def rollback(self):
        self._conn.rollback()

    def __del__(self):
        try:
            self._cursor.close()
            self._conn.close()
        except:
            pass

    def close(self):
        self.__del__()


db = DBReport()
db.create_table()
# 指定要抓取的url
page_url = 'https://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/'
print(page_url)
# # query the website and return the html to the variable 'page'
page = urllib.request.urlopen(page_url)
# print(page)
# # parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'lxml')
# print(soup)
# find results within table
table = soup.find('table', attrs={'class': 'tableSorter'})
# print(table)
results = table.find_all('tr')
# print(results)
print('Number of results', len(results))
# create and write headers to a list
rows = []
rows.append(['Rank', 'Company Name', 'Webpage', 'Description', 'Location', 'Year end', 'Annual sales rise over 3 years',
             'Sales', 'Staff', 'Comments'])
# loop over results
for result in results:
    # find all columns per result
    data = result.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue

    rank = data[0].getText()
    company = data[1].getText()
    location = data[2].getText()
    yearend = data[3].getText()
    salesrise = data[4].getText()
    sales = data[5].getText()
    staff = data[6].getText()
    comments = data[7].getText()

    # extract description from the name
    companyname = data[1].find('span', attrs={'class': 'company-name'}).getText()
    description = company.replace(companyname, '')

    # remove unwanted characters
    sales = sales.strip('*').strip('†').replace(',', '')
    # go to link and extract company website
    url = data[1].find('a').get('href')
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'lxml')
    # parse the html using beautiful soup and store in variable 'soup'
    try:
        tableRow = soup.find('table').find_all('tr')[-1]
        webpage = tableRow.find('a').get('href')
    except Exception as e:
        webpage = None
    print(webpage)
    datas = (rank, companyname, webpage, description, location, yearend, salesrise, sales, staff, comments)
    db.insert_data(datas)
    # write each result to rows
    rows.append([rank, companyname, webpage, description, location, yearend, salesrise, sales, staff, comments])
print(rows)
db.close()
## Create csv and write rows to output file
with open('techtrack100.csv', 'w', newline='',encoding='utf-8',errors='replace')as fp:
    csv_output = csv.writer(fp)
    csv_output.writerows(rows)
print('csv文件已写好')
