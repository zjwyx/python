from django.db import models

# Create your models here.

# 用户表
class userInfo(models.Model):
    # 在数据库中生成自增的id主键
    id = models.AutoField(primary_key=True)
    # varchar()
    email = models.CharField(max_length=20)
    # varchar()
    password = models.CharField(max_length=30)


# 出版社表
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=18)

    def __str__(self):
        return self.name