#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

import requests
import itchat


def getRandomGreeting():
    response = requests.get("http://www.xjihe.com/api/life/greetings?festival=元旦&page=1",
                            headers={'apiKey': 'sQS2ylErlfm9Ao2oNPqw6TqMYbJjbs4g'})
    results = response.json()['result']
    greeting = results[random.randrange(len(results))]['words']
    return greeting


if __name__ == '__main__':
    # itchat.auto_login()
    # itchat.run()
    # friendList = itchat.get_friends(update=True)[1:]
    # greeting_list = []
    for i in range(100):
        msg = getRandomGreeting()
        print(msg)
        print(i)
        # greeting_list.append(msg)
    # print(len(friendList))
    # for num, friend in enumerate(friendList):
    #     print(friend['RemarkName'])
        # if friend['RemarkName'] in ['杨博', '润梅姐']:
        #     continue
        # print(friend['UserName'])
        # print(friend['NickName'])
        # itchat.send(random.choice(greeting_list), friendList[num]['UserName'])
        # friend.send((friend['NickName'] + '，' + getRandomGreeting()))
        # print('send success!')
