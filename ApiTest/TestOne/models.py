from django.db import models


# Create your models here.

# 吐槽表
class TuCao(models.Model):
    user = models.CharField(max_length=32, null=True)  # 吐槽人姓名
    text = models.CharField(max_length=1024, null=True)  # 吐槽内容
    create_time = models.DateTimeField(auto_now=True)  # 创建时间

    def __str__(self):
        return f'{self.text}  {str(self.create_time)}'
