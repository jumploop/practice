#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

import requests
import random
import time

headers = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}


def get_json(url, num):
    params = {
        'page_size': 10,
        'next_offset': str(num),
        'tag': '今日热门',
        'platform': 'pc'
    }

    try:
        html = requests.get(url, params=params, headers=headers)
        return html.json()

    except Exception as e:
        print('request error')
        pass


def filter_emoji(desstr, restr=''):
    '''
    过滤表情
    '''
    try:
        co = re.compile(
            u"(\ud83d[\ude00-\ude4f])|"  # emoticons
            u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
            u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
            u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
            u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
            "+", flags=re.UNICODE)
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub(restr, desstr)


def download(url, path):
    start = time.time()  # 开始时间
    size = 0
    time.sleep(2)
    response = requests.get(url, headers=headers, stream=True)  # stream属性必须带上
    chunk_size = 1024  # 每次下载的数据大小
    content_size = int(response.headers['content-length'])  # 总大小
    if response.status_code == 200:
        print('[文件大小]:%0.2f MB' % (content_size / chunk_size / 1024))  # 换算单位
        with open(path, 'wb') as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                size += len(data)  # 已下载的文件大小
    total = time.time() - start
    print('total time: %.2fs' % total)


def main():
    for i in range(10):
        url = 'http://api.vc.bilibili.com/board/v1/ranking/top?'
        num = i * 10 + 1
        html = get_json(url, num)
        infos = html['data']['items']
        for info in infos:
            title = info['item']['description'].strip()  # 小视频的标题
            video_url = info['item']['video_playurl']  # 小视频的下载链接
            print(title)
            title = filter_emoji(title).replace('(>\u0602<）', '').replace('\n', '')
            # 为了防止有些视频没有提供下载链接的情况
            path = r'F:\bilibili\video'
            if not os.path.exists(path):
                os.makedirs(path)
            file_name = os.path.sep.join([path, '{}.mp4'.format(''.join(title.split()))])
            try:
                download(video_url, file_name)
                print('成功下载一个!')
            except Exception as e:
                print('凉凉,下载失败')
                pass

        time.sleep(int(format(random.randint(2, 8))))  # 设置随机等待时间


if __name__ == '__main__':
    main()
