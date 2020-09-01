#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import datetime
 
sender = 'from@vzoom.com'
receivers = ['1300945503@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("Xshell", 'utf-8')
message['To'] =  Header("监控专用邮箱", 'utf-8')
subject = 'Data Monitor'
message['Subject'] = Header(subject, 'utf-8')
 
#邮件正文内容
time_today = datetime.datetime.now() + datetime.timedelta(minutes=16)
time_today = time_today.strftime("%Y-%m-%d %H:%M:%S")
message.attach(MIMEText('数据监控 {}'.format(time_today), 'plain', 'utf-8'))
 
# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('/root/for_monitor/for_monitor.zip', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="for_monitor.zip"'
message.attach(att1)

def record(flag):
    try:
        with open('email_log.txt','a+') as f:
            if flag == 1:
                f.write('邮件发送成功...%s' % datetime.datetime.now() + '\r\n')
            elif flag == 0:
                f.write('邮件发送失败...%s' % datetime.datetime.now() + '\r\n')
    except Exception:
        with open('email_log.txt','w') as f:
            if flag == 1:
                f.write('邮件发送成功...%s' % datetime.datetime.now() + '\r\n')
            elif flag == 0:
                f.write('邮件发送失败...%s' % datetime.datetime.now() + '\r\n')


if __name__ == '__main__':
    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功"
        record(1)
    except smtplib.SMTPException:
        print "Error: 无法发送邮件"
        record(0)


