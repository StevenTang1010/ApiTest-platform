"""ApiTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from TestOne.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', welcome),  # 欢迎页面
    re_path('^home/(?P<page>.+)/(?P<oid>.*)/$', home),  # 主页
    path('login/', login),  # 登录页面
    path('login_action/', login_action),  # 执行登录接口
    path('accounts/login/', login),  # 非登录状态自动跳回登录页面
    path('logout/', logout),  # 非登录状态自动跳回登录页面
    path('pei/', pei),  # 非登录状态自动跳回登录页面
    path('help/', help_doc),  # 非登录状态自动跳回登录页面
    path('prj_list/', projects),  # 非登录状态自动跳回登录页面
    path('delete_project/', delete_project),  # 删除项目逻辑接口
    path('add_project/', add_project),  # 添加项目逻辑接口
    re_path('^apis/(?P<id>.*)/$', open_apis),  # 进入api接口库
    re_path('^prj_api_add/(?P<pid>.*)/$', prj_api_add),  # 新增接口
    re_path('^prj_api_del/(?P<aid>.*)/$', prj_api_del),  # 删除接口
    re_path('^cases/(?P<id>.*)/$', cases),  # 进入用例库
    re_path('^prj_setting/(?P<id>.*)/$', prj_setting),  # 进入项目设置
    re_path('^save_prj_setting/(?P<id>.*)/$', save_prj_setting),  # 进入项目设置
]
