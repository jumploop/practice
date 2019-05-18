#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wechatsogou
import json
from pprint import pprint

# 可配置参数

# 直连
from wechatsogou import WechatSogouConst

ws_api = wechatsogou.WechatSogouAPI()

# 验证码输入错误的重试次数，默认为1
# ws_api = wechatsogou.WechatSogouAPI(captcha_break_time=31)

# 所有requests库的参数都能在这用
# 如 配置代理，代理列表中至少需包含1个 HTTPS 协议的代理, 并确保代理可用
# ws_api = wechatsogou.WechatSogouAPI(proxies={
#     "http": "127.0.0.1:8888",
#     "https": "127.0.0.1:8888",
# })

# 如 设置超时
# ws_api = wechatsogou.WechatSogouAPI(timeout=0.1)

# 获取特定公众号信息 - get_gzh_info
ret = ws_api.get_gzh_info('CSDN')
print(ret)

# 搜索公众号
ret = ws_api.search_gzh('南京航空航天大学')
print(ret)
# 搜索微信文章
ret = ws_api.search_article('南京航空航天大学')
print(ret)

# 解析最近文章页 - get_gzh_article_by_history
ret = ws_api.get_gzh_article_by_history('南航青年志愿者')
print(ret)

# 解析 首页热门 页 - get_gzh_article_by_hot
gzh_articles = ws_api.get_gzh_article_by_hot(WechatSogouConst.hot_index.food)
for i in gzh_articles:
    pprint(i)
# 获取关键字联想词
ret=ws_api.get_sugg('高考')
print(ret)