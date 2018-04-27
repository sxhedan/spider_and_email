#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText

title = 'news test'
with open('news.txt','r') as f:
    news_data = f.read()
f.close()
message = MIMEText(news_data, 'plain', 'utf-8')

message['From'] = 'Dan <testdan79@gmail.com>'
message['To'] = 'Dan <sxhedan@gmail.com>'
message['Cc'] = ''
message['Subject'] = 'News'

msg_full = message.as_string()

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login('testdan79@gmail.com', 'itsatestaccount')
server.sendmail('testdan79@gmail.com',
                ['testdan79@gmail.com'],
                msg_full)
server.quit()
