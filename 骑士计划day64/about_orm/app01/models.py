from django.db import models

# Create your models here.


# 创建一个自定义的字段类型
class MyCharField(models.Field):
    def __init__(self,max_length,*args,**kwargs):
        super(MyCharField,self).__init__(max_length=max_length)
        self.max_length = max_length

    def db_type(self, connection):
        return 'char(%s)'% self.max_length

class UserInfo(models.Model):
    name = MyCharField(max_length=12)
    birthday = models.DateTimeField(verbose_name='生日')
    gender = models.SmallIntegerField(choices=((1,'男'),(2,'女'),(3,'保密')),default=3)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=32)
    push_time = models.DateTimeField(auto_now_add=True)   # 发布时间，在数据库中创建这条记录的时间
    edit_time = models.DateTimeField(auto_now=True)   # 最后修改的时间