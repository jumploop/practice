import random
from threading import Timer
import threading
import requests
from bs4 import BeautifulSoup
from wxpy import *

# linux执行登陆请调用下面的这句
bot = Bot(console_qr=2, cache_path="botoo.pkl")
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",

}


def getWeather(city_code):
    try:
        url = 'http://www.weather.com.cn/weather/{}.shtml'.format(city_code)
        resp = requests.get(url, headers=headers)
        # print(resp.text)
    except BaseException as e:
        print(e)
        return {}

    # getWeather(101110101)
    soup = BeautifulSoup(resp.content.decode('utf-8'), 'html.parser')
    tagToday = soup.find('p', class_="tem")  # 第一个包含class="tem"的p标签即为存放今天天气数据的标签
    try:
        temperatureHigh = tagToday.span.string  # 有时候这个最高温度是不显示的，此时利用第二天的最高温度代替。
    except AttributeError:
        temperatureHigh = tagToday.find_next('p', class_="tem").span.string  # 获取第二天的最高温度代替

    temperatureLow = tagToday.i.string  # 获取最低温度
    weather = soup.find('p', class_="wea").string  # 获取天气
    wind = soup.find('p', class_="win")  # 获取风力
    clothes = soup.find('li', class_="li3 hot")  # 穿衣指数
    return {'温度': '{}/{}'.format(temperatureHigh, temperatureLow), '天气': weather, '风力': wind.i.string,
            '穿衣': clothes.a.span.string + ',' + clothes.a.p.string}


def strDic(dic):
    str_weather = ''
    for key in dic:
        str_weather += key + ':' + dic[key]
        str_weather += '\n'
    return str_weather


def sendWeatherMsg(friend, msg):
    try:

        # 你朋友的微信名称，不是备注，也不是微信帐号。
        my_friend = bot.friends().search(friend)[0]
        my_friend.send(msg)
        # 每86400秒（1天），发送1次
        t = Timer(86400, sendWeatherMsg)
        # 为了防止时间太固定，于是决定对其加上随机数
        ran_int = random.randint(0, 100)
        t = Timer(86400 + ran_int, sendWeatherMsg)
        t.start()
    except:

        # 你的微信名称，不是微信帐号。
        my_friend = bot.friends().search('杀破狼')[0]
        my_friend.send(u"今天消息发送失败了")


if __name__ == '__main__':
    dic = getWeather(101110101)
    msg = strDic(dic)
    receivers = ['婺愇囉茻', '一叶知秋', '开心公举 คิดถึง']
    threads=[]
    num=len(threads)
    for friend in receivers:
        t=threading.Thread(target=sendWeatherMsg,args=(friend,msg))
        threads.append(t)
    for i in range(num):
        threads[i].start()
    for i in range(num):
        threads[i].join()
