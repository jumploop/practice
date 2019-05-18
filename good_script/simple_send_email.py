#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yagmail

# 链接邮箱服务器
yag = yagmail.SMTP(user='982698078@qq.com', password='****', host='smtp.qq.com')
# 邮件正文
contents = ['this is a python send mail test!', 'you can find a apple', 'apple']
# 发送邮件
resp = yag.send('827182486@qq.com', 'object', contents)
print(resp)
