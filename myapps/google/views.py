from django.shortcuts import render

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
        html = etree.HTML(res.text)
        content = html.xpath("")
        content.replace('href="','href="/google/search/?href=')
        content.replace('<form style="display:block;margin:0;background:none" action="/search" id="tsf" method="GET" name="gs"><table border="0" cellpadding="0" cellspacing="0" style="margin-top:20px;position:relative"><tr><td><div class="lst-a"><table cellpadding="0" cellspacing="0"><tr><td class="lst-td" width="555" valign="bottom"><div style="position:relative;zoom:1"><input class="lst" value="python" title="搜索" autocomplete="off" id="sbhost" maxlength="2048" name="q" type="text"></div></td></tr></table></div></td><td><div class="ds"><div class="lsbb"><button class="lsb" value="搜索" name="btnG" type="submit"><span class="sbico" style="background-image:url(/images/nav_logo229.png);background-repeat:no-repeat;height:14px;width:13px;display:block;background-position:-36px -111px"></span></button></div></div></td></tr></table><input name="safe" value="strict" type="hidden"><input name="hl" value="zh-CN" type="hidden"></form>','')
        return render(request, 'google/search.html',{"content": content})
