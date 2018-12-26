from lib.adduser_email import sendEmail as add_mail
from celery import task


@task
def register_mail(email, username, password):
    add_mail([email], 'DataMing管理系统账号注册成功', 'hi,{0},DataMing管理系统账号开通成功,你的密码:{1},登录地址：http://admin.dm.xywy.com/login/'.format(username,password))


@task
def set_passward_mail(email, username, password):
    add_mail([email], 'DataMing管理系统密码修改成功', 'hi,{0},DataMing管理系统账号密码修改成功,你的新密码:{1},登录地址：http://admin.dm.xywy.com/login/'.format(username,password))