#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

common_url = 'http://www.imomoe.io'
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}


def get_animations_urls():
    """获取最新的动漫"""
    try:
        html = requests.get(common_url, headers=headers).content
    except Exception as e:
        print(str(e))
        return
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)
    result = soup.find('div', attrs={'class': 'imgs'})
    # print(result)
    lis = result.find_all('li')
    ps = [li.find('p') for li in lis]
    print(ps)
    hrefs = [p.find('a') for p in ps]
    # for li in lis:
    urls = []
    for href in hrefs:
        url = href.get('href')
        title = href.get_text()
        print(title)
        urls.append((title, ''.join((common_url, url))))
    print(urls)
    return urls


def get_appoint_animation(url):
    try:
        html = requests.get(url, headers=headers).content
    except Exception as e:
        print(str(e))
        return
    soup = BeautifulSoup(html, 'lxml')
    result = soup.find_all('div', attrs={'class': 'movurl'})[-1] if len(
        soup.find_all('div', attrs={'class': 'movurl'})) > 0 else None
    if  result is None:
        return
    href = result.find_all('a')[-1]
    print(href)
    title = href.get_text()
    print(title)
    u = ''.join((common_url, str(href.get('href'))))
    return title, u
    # print(result)


def download_animation(title,url):
    try:
        html = requests.get(url, headers=headers,stream=True)
    except Exception as e:
        print(str(e))
        return
    chunk_size = 1024  # 每次下载的数据大小
    with open('{}.mp4'.format(title), 'wb')as file:
        for data in html.iter_content(chunk_size=chunk_size):
            file.write(data)


def main():
    # 获取最新动漫的url
    urls = get_animations_urls()
    if urls is None:
        return
    appoint_urls = []
    for title, url in urls:
        ret = get_appoint_animation(url)
        if ret is None:
            continue
        appoint_urls.append((title + ret[0], ret[1]))
    print(appoint_urls)
    for t,u in appoint_urls:
        download_animation(t,u)


if __name__ == '__main__':
    main()
