from django.shortcuts import render
import re
# Create your views here.
import requests
import json
import traceback
from django.shortcuts import render, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from rbac.forms import LoginForm, RegistForm, SetPasswordForm
from rbac import models
from rbac.service.init_permission import init_permission
from django.views.decorators.cache import cache_page  # 导入设置缓存的装饰器
from django.conf import settings
from lib.decorator import save_request_url
from rbac.email_task import register_mail,set_passward_mail
from lib.validate import validate
from lxml import etree

@validate
@save_request_url
def search(request, last_url):
    if request.method == 'GET':
        return render(request, 'google/search.html')
    else:
        content = request.POST.get('content')
        url = 'https://www.google.com.hk/search?safe=strict&hl=zh-CN&q={0}'
        res = requests.get(url.format(content))
        # html = etree.HTML(res.text)
        # content = html.xpath('//body')[0]

        content = res.text
        print('href="' in content)
        # print(re.sub())

        return render(request, 'google/search.html',{"content": content})


@save_request_url
def click(request, last_url):
    if request.method == 'GET':
        print('click')
        print(request.get_full_path())
        url = 'https://www.google.com.hk'+ request.get_full_path()
        print('url',url)
        res = requests.get(url)

        # html = etree.HTML(res.text)
        content = res.text


        return render(request, 'google/search.html', {"content": content})
