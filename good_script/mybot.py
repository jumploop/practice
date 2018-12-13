# coding: utf-8
from __future__ import unicode_literals

from wechat_sender import listen
from wxpy import *

bot = Bot(cache_path=True)
receivers = []
receivers.append(bot.file_helper)
receivers.append(bot.friends().search()[0])
# receivers.append(ensure_one(bot.friends().search('李静', city='西安')))  # 有可能搜索出多个结果
receivers.append(bot.friends().search('一叶知秋')[0])
# receivers.append(bot.friends().search('妈')[0])
print(receivers)
listen(bot, receivers=receivers, token='weather_report_123456789')  # 关键一步