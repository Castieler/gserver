import smtplib
from email.mime.text import MIMEText
from conf.email_conf import ADDUSER_MAIL_PASS,ADDUSER_MAIL_HOST,ADDUSER_MAIL_SENDER,ADDUSER_MAIL_USER

def sendEmail(receivers,title, content):
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(ADDUSER_MAIL_SENDER)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(ADDUSER_MAIL_HOST, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(ADDUSER_MAIL_USER, ADDUSER_MAIL_PASS)  # 登录验证
        smtpObj.sendmail(ADDUSER_MAIL_SENDER, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)


if __name__ == '__main__':
    sendEmail('十万关键词数据灌贴项目', '数据已处理并提供，数据量：72211')
