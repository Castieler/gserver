#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliangyy
@license: MIT Licence
@contact: liangliangyy@gmail.com
@site: https://www.lylinux.org/
@software: PyCharm
@file: urls.py
@time: 2016/11/12 下午3:03
"""

from django.urls import path
from . import views

app_name = "rabc"
urlpatterns = [
    # url(r'^po456stcomment/(?P<article_id>\d+)$', views.CommentPostView.as_view(), name='postcomment'),
    #
    path(r'search/', views.search, name='search'),
    path(r'', views.click, name='click'),

    #
    # path(r'regist/', views.regist, name='regist'),
    # path(r'set_pwd/', views.set_password, name='set_pwd'),
    # path(r'out/', views.out, name='out'),
    # path(r'home/', views.home, name='home'),
]
