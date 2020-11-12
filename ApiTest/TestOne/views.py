from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from TestOne.models import DB_TuCao, DB_HomeHref, DB_Project, DB_Apis


# Create your views here.
# 基础页面
@login_required
def welcome(request):
    return render(request, 'base_page.html', {'page': 'home.html', 'oid': ''})


# 首页
@login_required
def home(request, page, oid):
    res = page_json(page, oid)
    return render(request, page, res)


# 控制不同的页面返回不同的数据：数据分发器
def page_json(page, oid=''):
    res = {}
    if page == 'home.html':
        # 返回传送门内容
        hrefs = DB_HomeHref.objects.all()
        # 返回项目列表
        projects = DB_Project.objects.all()
        res = {'hrefs': hrefs, 'projects': projects}
    elif page == 'prj_list.html':
        projects = DB_Project.objects.all()
        res = {'projects': projects}
    elif page == 'prj_apis.html':
        project = DB_Project.objects.filter(id=oid)[0]
        apis = DB_Apis.objects.filter(prj_id=oid)
        res = {'project': project, 'apis': apis}
    elif page == 'prj_cases.html':
        project = DB_Project.objects.filter(id=oid)[0]
        res = {'project': project}
    elif page == 'prj_setting.html':
        project = DB_Project.objects.filter(id=oid)[0]
        res = {'project': project}

    return res


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
    DB_TuCao.objects.create(user=request.user.username, text=tucao_text)
    return HttpResponse('')


# 返回项目列表
def projects(request):
    return render(request, 'base_page.html', {'page': 'prj_list.html', 'oid': ''})


# 返回项目列表
def delete_project(request):
    id = request.GET['id']
    DB_Project.objects.filter(id=id).delete()
    return HttpResponse('')


# 返回项目列表
def add_project(request):
    project_name = request.GET['project_name']
    project_remark = request.GET['project_remark']
    DB_Project.objects.create(name=project_name, remark=project_remark, user=request.user.username, other_user='')
    return HttpResponse('')


# 进入api接口库
def open_apis(request, id):
    prj_id = id
    return render(request, 'base_page.html', {'page': 'prj_apis.html', 'oid': prj_id})


# 新增单条接口逻辑
def prj_api_add(request, pid):
    prj_id = pid
    db_dict = {
        'prj_id': prj_id,
        'api_name': 'models.CharField(max_length=100, null=True)',
        'api_method': 'models.CharField(max_length=10, null=True)',
        'api_url': 'models.CharField(max_length=1000, null=True)',
        'api_header': 'models.CharField(max_length=1000, null=True)',
        'api_host': 'models.CharField(max_length=100, null=True)',
        'api_login': 'models.CharField(max_length=10, null=True)  # 是否带登录状态',
        'des': 'models.CharField(max_length=1000, null=True)  # 描述',
        'body_code': 'models.CharField(max_length=20, null=True)  # 请求体编码格式',
        'api_body': 'models.CharField(max_length=1000, null=True)  # 请求体',
        'result': 'models.TextField(null=True)  # 返回体，可能很长，用大文本存储',
        'sign': 'models.CharField(max_length=10, null=True)  # 是否启用自定义算法加密',
        'file_key': 'models.CharField(max_length=50, null=True)  # 文件key',
        'file_name': 'models.CharField(max_length=50, null=True)  # 文件名',
        'public_header': 'models.CharField(max_length=1000, null=True)  # 全局变量-公共请求头',
    }
    DB_Apis.objects.create(prj_id=prj_id)
    return HttpResponseRedirect(f'/apis/{prj_id}/')


# 删除单条接口逻辑
def prj_api_del(request, aid):
    prj_id = DB_Apis.objects.filter(id=aid)[0].prj_id
    DB_Apis.objects.filter(id=aid).delete()
    return HttpResponseRedirect(f'/apis/{prj_id}/')


# 进入用例设置
def cases(request, id):
    prj_id = id
    return render(request, 'base_page.html', {'page': 'prj_cases.html', 'oid': prj_id})


# 进入项目设置
def prj_setting(request, id):
    prj_id = id
    return render(request, 'base_page.html', {'page': 'prj_setting.html', 'oid': prj_id})


# 进入项目设置
def save_prj_setting(request, id):
    prj_id = id
    prj_name = request.GET['prj_name']
    prj_remark = request.GET['prj_remark']
    other_user = request.GET['other_user']
    DB_Project.objects.filter(id=prj_id).update(name=prj_name, remark=prj_remark, other_user=other_user)
    return HttpResponse('')


# 帮助文档
def help_doc(request):
    return render(request, 'base_page.html', {'page': 'help.html', 'oid': ''})
