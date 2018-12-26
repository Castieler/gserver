# coding:utf-8
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


def login(request):
    if request.method == 'GET':
        try:
            del request.session["username"]
            del request.session["icon_url"]
        except:
            pass
        form = LoginForm()
        return render(request, 'rbac/login.html', {"form": form})
    elif request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            print(username)
            password = form.cleaned_data['password']
            user_queryset = models.User.objects.filter(username=username).values('password_hash')
            print(password)
            try:
                password_hash = user_queryset[0].get('password_hash', '')
            except:
                return render(request, 'rbac/login.html', {"info": "该账户未注册"})

            if models.User().verify_password(password_hash, password):
                _user_queryset = models.User.objects.filter(username=username)
                request.session['username'] = str(_user_queryset[0])
                request.session.set_expiry(60 * 30)
                init_permission(_user_queryset[0], request)
                _url_list = []
                for item in request.session[settings.MENU_LIST]:
                    _url_list.append(item['url'])
                if '/rbac/home/' in _url_list:
                    return redirect('/rbac/home/')
                else:
                    return redirect(_url_list[0])
            else:
                return render(request, 'rbac/login.html', {"info": "密码错误"})
        else:
            return render(request, 'rbac/login.html', {"form": form})


def regist(request):
    if request.method == 'GET':
        form = RegistForm()
        return render(request, 'rbac/regist.html', {"form": form})
    elif request.method == 'POST':
        form = RegistForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']  # cleaned_data类型是字典，里面是提交成功后的信息
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user_queryset = models.User.objects.filter(username=username)
            if user_queryset:
                return render(request, "rbac/regist.html", {"errors": {'username': ['此用户名已存在，请更换']}})
            else:
                password_hash = str(generate_password_hash(password))
                models.User.objects.create(username=username, password_hash=password_hash,email=email)
                a = models.User.objects.get(username=username)
                xuesheng = models.Role.objects.all()
                try:
                    a.roles.add(xuesheng[0])
                except IndexError:
                    print('添加权限失败')
                register_mail.delay(email, username, password)
                return render(request, "rbac/login.html", {"info": '注册成功'})

        else:
            return render(request, "rbac/regist.html", {"errors": form.errors})

@validate
@save_request_url
def set_password(request, last_url):
    if request.method == 'GET':
        icon_url = request.session.get('icon_url', None)
        if not icon_url:
            request.session['icon_url'] = last_url
        return render(request, 'rbac/set_pwd.html', {"icon_url": request.session['icon_url']})
    elif request.method == 'POST':
        form = SetPasswordForm(data=request.POST)
        if form.is_valid():
            username = request.session['username']
            password = form.cleaned_data['password']
            password_hash = str(generate_password_hash(password))
            models.User.objects.filter(username=username).update(password_hash=password_hash)
            try:
                email = models.User.objects.filter(username=username).values('email')[0]['email']
                if email:
                    set_passward_mail.delay(email, username, password)
            except:
                traceback.print_exc()
            return render(request, 'rbac/set_pwd.html', {"info": "已修改，请牢记密码", "icon_url": request.session['icon_url']})

        else:
            return render(request, 'rbac/set_pwd.html',
                          {"errors": form.errors, "icon_url": request.session['icon_url']})

@validate
@save_request_url
def home(request, last_url):
    return render(request, 'rbac/home.html')


@validate
@save_request_url
def out(request, last_url):
    if request.method == 'GET':
        try:
            del request.session["username"]
            del request.session["icon_url"]
        except:
            pass
        request.session.clear()
    return redirect('/rbac/login/')


def page_not_found(request):
    return render(request, 'error/404.html')


def page_error(request):
    return render(request, 'error/500.html')
