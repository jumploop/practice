#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yagmail

# 链接邮箱服务器
# yag = yagmail.SMTP(user='982698078@qq.com', password='kppqdasgcuwibbhc', host='smtp.qq.com')
yag = yagmail.SMTP(user='liming_201314521@163.com', password='lm201314', host='smtp.163.com')

# 邮件正文
# contents = ['this is a python send mail test!', 'you can find a apple', 'apple']
msg="""
事实上，此代码并不复杂，只要您了解电子邮件的使用，那么您必须考虑以下问题：

您的登录电子邮件帐户/密码

对方的电子邮件帐户

电子邮件内容（标题、正文、附件）

邮件服务器（smtp.xxx.com/pop3.xxx.com）

如果你想在电子邮件的正文中嵌入图像怎么办？你能在HTML邮件中直接链接图像地址吗？答案是，大多数电子邮件服务自动阻止图像与外部链接，因为他们不知道链接是否指向恶意网站。

为了将图像嵌入到电子邮件的正文中，我们只需按照发送的方式添加电子邮件作为附件，然后我们可以通过引用src=“cid:0”将图像作为附件嵌入到HTML中。如果您有多个图像，请逐个编号，然后参考不同的cid:x。

小编推荐一个学python的学习qun 232,550246

无论你是大牛还是小白，是想转行还是想入行都可以来了解一起进步一起学习！裙内有开发工具，很多干货和技术资料分享！

作者：小二二
链接：https://zhuanlan.zhihu.com/p/55797461
来源：知乎
著作权归作者所有，转载请联系作者获得授权。"""
# 发送邮件
yag.send('827182486@qq.com', 'object', contents=msg)
# 给多个用户发邮件：
# 只需要将接收邮箱 变成一个list即可。
# yag.send(['liming_201314521@163.com','liming_201314@126.com'], 'test', contents=msg)
