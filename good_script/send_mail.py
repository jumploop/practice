#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename：send_mail.py

import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr, formatdate
import sys


# from email.mime.application import MIMEApplication
# import os.path
def format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def sendmail(f_from, f_to, f_cclist, content_info, f_subject):
    # From = f_from
    # To = f_to
    # file_name = f_file_name

    server = smtplib.SMTP("smtp.qq.com")
    server.set_debuglevel(1)
    server.login("982698078@qq.com", "password")

    # 构造MIMEMultipart对象做为根容器
    main_msg = MIMEMultipart()

    text_msg = MIMEText("您好!<br>"
                        + content_info.title() +
                        "<br>任凤军 <br>"
                        "xx技术股份有限公司 <br>"
                        "手机: xx<br>"
                        "座机：xxx<br>"
                        "邮箱：xxxx@xx.com<br>"
                        "地址：xxxx<br>"
                        "邮编：130011<br>"
                        "===================================<br>"
                        "", 'HTML', 'utf-8')
    main_msg.attach(text_msg)

    # xlsxpart = MIMEApplication(open(file_name, 'rb').read())
    # xlsxpart.add_header('Content-Disposition', 'attachment', filename=f_subject+".docx")
    # main_msg.attach(xlsxpart)
    # 设置根容器属性
    main_msg['From'] = format_addr('Python爱好者 <%s>' % f_from)
    main_msg['To'] = format_addr('管理员 <%s>' % f_to)
    main_msg['Cc'] = ",".join(f_cclist)
    main_msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
    main_msg['Date'] = formatdate()
    # f_cclist为完整的需要接收邮件的列表，原本只存放抄送列表，这里需要添加上收件人
    f_cclist.append(f_to)
    # 得到格式化后的完整文本
    fullText = main_msg.as_string()

    # 用smtp发送邮件
    try:
        server.sendmail(f_from, f_cclist, fullText)
        print('mail send success!')
    except Exception as e:
        print('mail send fail!' + str(e))
    finally:
        server.quit()


if __name__ == "__main__":
    # sys.setdefaultencoding('utf-8')
    message = [
        'Usage:',
        '      sendmail.py "topic" "mail body text" "mail to"',
        'Examples of usage:',
        '                  sendmail.py "topic" "hello world" "14638852@qq.com"',
    ]
    try:
        topic = '年终总结'  # str(sys.argv[1]).encode("utf-8")
        content = 'hello world!'  # str(sys.argv[2]).encode("utf-8")
        mailto = '827182486@qq.com'  # str(sys.argv[3]).encode("utf-8")
    except IndexError:
        for line in message:
            print(line + '\n')
        sys.exit()
    cclist = []
    # clist =[]
    sendmail("982698078@qq.com", mailto, cclist, content, topic)
"""
备注：
sendmail("xxxx@gmail.com", mailto, cclist, content, topic)
发件人，收件人，抄送列表，正文内容，邮件标题
Usage:
sendmail.py
"topic" "mail body text" "mail to"
Examples
of
usage:
sendmail.py
"topic" "hello world" "14638852@qq.com"
"""