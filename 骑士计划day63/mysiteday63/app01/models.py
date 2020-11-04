from django.db import models

# Create your models here.

# 用户表
class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)