#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time

import requests
import itchat


def getRandomGreeting():
    response = requests.get("http://www.xjihe.com/api/life/greetings?festival=元宵&page=4",
                            headers={'apiKey': 'sQS2ylErlfm9Ao2oNPqw6TqMYbJjbs4g'})
    results = response.json()['result']
    print(results)
    greeting = results[random.randrange(len(results))]['words']
    # greeting = [results[i]['words'] for i in range(len(results))]
    # print(greeting)
    return greeting


if __name__ == '__main__':
    itchat.auto_login()
    friendList = itchat.get_friends(update=True)[1:]
    # greeting_list = []
    # for i in range(10):
    #     msg = getRandomGreeting()
    #     print(msg)
    #     print(i)
    # greeting_list.append(msg)
    print(len(friendList))
    for num, friend in enumerate(friendList):
        print(friend['RemarkName'])
        # if friend['RemarkName'] in ['杨博', '润梅姐']:
        #     continue
        print(friend['UserName'])
        print(friend['NickName'])
        print(num)
        # itchat.send(random.choice(greeting_list), friendList[num]['UserName'])
        # friend.send((friend['NickName'] + '，' + getRandomGreeting()))
        time.sleep(1)
        friend.send((getRandomGreeting()))
        print('send success!')
