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


@validate
@save_request_url
def search(request, last_url):
    if request.method == 'GET':
        return render(request, 'google/search.html')
    else:
        es_name = request.POST.get('content')
        print(es_name)
        return render(request, 'google/search.html')
