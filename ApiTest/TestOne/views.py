from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from TestOne.models import TuCao


# Create your views here.
# 基础页面
@login_required
def welcome(request):
    return render(request, 'base_page.html', {'page': 'home.html', 'oid': ''})


# 首页
@login_required
def home(request, page, oid):
    return render(request, page)


# 登录页面
def login(request):
    return render(request, 'login.html')


# 执行登录
def login_action(request):
    username = request.GET['username']
    password = request.GET['password']

    # 开始连接数据库验证用户名密码的正确性
    from django.contrib import auth
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        # 进行正确的动作
        auth.login(request, user)
        request.session['user'] = username
        return HttpResponse('True')
    else:
        # 返回前端用户名密码不正确
        return HttpResponse('False')


# 退出登录
def logout(request):
    from django.contrib import auth
    auth.logout(request)
    return HttpResponseRedirect('/login/')


# 吐槽
def pei(request):
    tucao_text = request.GET['tucao_text']
    TuCao.objects.create(user=request.user.username, text=tucao_text)
    return HttpResponse('')


# 帮助文档
def help_doc(request):
    return render(request, 'base_page.html', {'page': 'help.html', 'oid': ''})
