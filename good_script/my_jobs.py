from threading import Timer

from wxpy import ResponseError

from good_script import city_code
from good_script.send_weather_message_to_weixinfriends import getWeather, strDic, sendWeatherMsg


class MyJob(object):
      def __sendWeatherMsg(self):
          for my_job in self.my_jobs:
              code = city_code.find_code(my_job['city'])
              wea = getWeather(code)
              strWea = strDic(wea)
              title = '{}天气预报：\n'.format(my_job['city'])
              sendWeatherMsg(my_job['receivers'], title + strWea)#发送天气信息给文件助手

     def addMyJobs(self, json_job):
         self.my_jobs = json_job['items']
         scheduler = BackgroundScheduler()
         scheduler.add_job(self.__sendWeatherMsg, trigger = 'cron', hour = json_job['hour']
         # , minute = json_job['minute'], second = '5,10,15,20,25,30,35,40,45,50,55')
         scheduler.start()


city_code = city_code.City()
city_code.load('city_code.txt')

if __name__ == "__main__":
    my_jobs = {
        "id": "my_jobs",
        "hour": "6, 17",
        "minute": "30",
        "items": [{
            "receivers": "文件传输助手,李静,拉卡拉",
            "city": "昌平"
        }, {
            "receivers": "文件传输助手,李静,拉卡拉",
            "city": "海淀"
        }]
    }
    try:
        ''' '''
        my_job = MyJob()
        my_job.addMyJobs(my_jobs)

        f = lambda x: lambda y: x + y
        t = Timer.Timer(f, 24 * 60 * 60)  # 创建线程 一天给自己发一条消息
        t.setDaemon(True)
        t.start()
        t.join()  # 防止主主线程退出

        # SendWeatherMsg(my_msg)

    except ResponseError as e:
        print(e.err_code, e.err_msg)  # 查看错误号和错误消息