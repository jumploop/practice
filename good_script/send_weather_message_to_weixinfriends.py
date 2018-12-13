import requests
from bs4 import BeautifulSoup
from wechat_sender import Sender, listen
from wxpy import Bot, ensure_one
from wechat_sender import listen
from wxpy import *



headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",

}


def getWeather(city_code):
    try:
        url = f'http://www.weather.com.cn/weather/{city_code}.shtml'
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
    return {'温度': f'{temperatureHigh}/{temperatureLow}', '天气': weather, '风力': wind.i.string,
            '穿衣': clothes.a.span.string + ',' + clothes.a.p.string}


def strDic(dic):
    str_weather = ''
    for key in dic:
        str_weather += key + ':' + dic[key]
        str_weather += '\n'
    return str_weather


def sendWeatherMsg(receivers, msg):
    try:

        # receivers = [u'拉卡拉', u'证明给他看', u'李静']
        # receivers = [u'拉卡拉', u'证明给他看', u'李静']
        ''' 
          #发送给指定好友 如果好友不存在 则发送给文件夹传输助手
          Sender(receivers = u'证明给他看').send(msg)
         Sender(receivers = u'拉卡拉').send(msg)
         Sender(receivers = u'李静').send(msg)
        '''
        # 发送给指定接收的用户
        # receivers = u'拉卡拉'
        # 接受者必须是监听对象的子集
        sender = Sender(receivers=receivers, token='weather_report_123456789')
        sender.send(msg)  # 如果没有指定receivers则发送给文件传输助手
        ''' 
        receivers = u'李静,情绕指尖'
        sender = Sender(receivers = receivers, token = 'weather_report_123456789')
              
       #有时候好使    有时候不好使
       sender.send_to('@wss', u'拉卡拉') #消息发送失败 会默认发送给receivers的第一个用户 Sender和Listen
       #sender.send_to(msg, u'证明给他看')
        '''

        # 测试控制命令

        '''
         receivers = u'拉卡拉'
         sender = Sender(receivers = receivers, token = 'weather_report_123456789')
         sender.send('@wss')#文如果没有指定receivers则发送给文件传输助手件传输助手
         '''
    except BaseException as e:
        print(e)


if __name__ == '__main__':
    bot = Bot(cache_path=True)
    receivers = []
    receivers.append(bot.file_helper)
    receivers.append(bot.friends().search()[0])
    # receivers.append(ensure_one(bot.friends().search('李静', city='西安')))  # 有可能搜索出多个结果
    receivers.append(bot.friends().search('一叶知秋')[0])
    # receivers.append(bot.friends().search('妈')[0])
    print(receivers)
    # receivers=[u'一叶知秋']
    dic = getWeather(101110101)
    wea = strDic(dic)
    sendWeatherMsg(receivers,wea)
    print(wea)
