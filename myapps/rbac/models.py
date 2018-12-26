#coding:utf-8
from django.db import models
# 密码散列及校验
from werkzeug.security import generate_password_hash, check_password_hash

class User(models.Model):
    """用户表
    普通字段:
        id, username, password
    关联字段:
        roles(多对多)
    """

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=16, verbose_name='用户名')
    password_hash = models.CharField(max_length=100, verbose_name='登录密码')
    email = models.CharField(max_length=100, default='', verbose_name='邮箱📮')
    vip = models.OneToOneField(to='VIP', null=True, default='', blank=True, verbose_name='用户是否是VIP',on_delete=models.CASCADE)
    pay = models.ForeignKey(to='UserPay',null=True, blank=True, default='', verbose_name='用户充值信息',on_delete=models.CASCADE)
    @staticmethod
    def verify_password(password_hash, password):
        return check_password_hash(password_hash, password)

    roles = models.ManyToManyField(to='Role', verbose_name='用户拥有的角色')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = '用户表'


class UserPay(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.CharField(max_length=30, default='', verbose_name='支付金额')
    stime = models.DateTimeField(auto_now_add=True, verbose_name='支付时间')
    month = models.CharField(max_length=30, default='', null=True,verbose_name='VIP充值月数')
    alipay_num = models.CharField(max_length=300, default='', null=True, verbose_name='支付宝订单号')
    weichat_num = models.CharField(max_length=300, default='', null=True, verbose_name='支付宝订单号')
    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = '用户充值表'

class VIP(models.Model):
    id = models.AutoField(primary_key=True)
    isvip = models.BooleanField(default=False, verbose_name='VIP')
    stime = models.DateTimeField(auto_now=True, verbose_name='VIP开始时间')
    etime = models.DateTimeField(auto_now=True, verbose_name='VIP开始时间')

    def __str__(self):
        return self.id
    class Meta:
        verbose_name_plural = 'VIP表'

class Role(models.Model):
    """角色表
    普通字段:
        id, title
    关联字段:
        permissions(多对多)
    """

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32, verbose_name='角色名')

    permissions = models.ManyToManyField(to='Permission', verbose_name='请选择角色拥有的权限：')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '角色表'


class Permission(models.Model):
    """权限表
    普通字段:
        id, url, feature
    关联字段:
        group(多对一), group_menu(自关联: 多对一)
    """

    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=64, verbose_name='权限url路径')
    feature = models.CharField(max_length=16, verbose_name='权限对应功能')
    display = models.BooleanField(default=True, verbose_name='权限是否显示在菜单栏')
    # group_menu = models.ForeignKey(to='Permission', to_field='id', verbose_name='组内菜单', null=True, blank=True, on_delete=models.CASCADE)
    group = models.ForeignKey(to='Group', to_field='id', verbose_name='所属权限组', on_delete=models.CASCADE)

    def __str__(self):
        return self.feature

    class Meta:
        verbose_name_plural = '权限表'


class Group(models.Model):
    """权限组表
    普通字段:
        id, title
    关联字段:
        menu(多对一)
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=16, verbose_name='权限组名')

    menu = models.ForeignKey(to='Menu', to_field='id', verbose_name='所属菜单', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '权限组表'


class Menu(models.Model):
    """菜单表
    普通字段: id, title
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=16)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '菜单表'
