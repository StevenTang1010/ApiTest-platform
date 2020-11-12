from django.db import models


# Create your models here.

# 吐槽表
class DB_TuCao(models.Model):
    user = models.CharField(max_length=32, null=True)  # 吐槽人姓名
    text = models.CharField(max_length=1024, null=True)  # 吐槽内容
    create_time = models.DateTimeField(auto_now=True)  # 创建时间

    def __str__(self):
        return f'{self.text}  {str(self.create_time)}'


# 超链接表
class DB_HomeHref(models.Model):
    name = models.CharField(max_length=32, null=True)  # 超链接名字
    href = models.CharField(max_length=1024, null=True)  # 超链接内容

    def __str__(self):
        return self.name


# 项目表
class DB_Project(models.Model):
    name = models.CharField(max_length=30, null=True)  # 项目名称
    remark = models.CharField(max_length=1000, null=True)  # 项目备注
    user = models.CharField(max_length=16, null=True)  # 项目创建者名字
    other_user = models.CharField(max_length=256, null=True)  # 项目其他创建者

    def __str__(self):
        return self.name


# 接口字段表
class DB_Apis(models.Model):
    prj_id = models.CharField(max_length=10, null=True)  # 项目id
    api_name = models.CharField(max_length=100, null=True)  # 接口名字
    api_method = models.CharField(max_length=10, null=True)  # 接口请求方式
    api_url = models.CharField(max_length=1000, null=True)  # 请求url
    api_header = models.CharField(max_length=1000, null=True)  # 请求头
    api_host = models.CharField(max_length=100, null=True)  # 请求域名
    api_login = models.CharField(max_length=10, null=True)  # 是否带登录状态
    des = models.CharField(max_length=1000, null=True)  # 描述
    body_code = models.CharField(max_length=20, null=True)  # 请求体编码格式
    api_body = models.CharField(max_length=1000, null=True)  # 请求体
    result = models.TextField(null=True)  # 返回体，可能很长，用大文本存储
    sign = models.CharField(max_length=10, null=True)  # 是否启用自定义算法加密
    file_key = models.CharField(max_length=50, null=True)  # 文件key
    file_name = models.CharField(max_length=50, null=True)  # 文件名
    public_header = models.CharField(max_length=1000, null=True)  # 全局变量-公共请求头

    def __str__(self):
        return self.prj_id
