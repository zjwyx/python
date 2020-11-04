from django.db import models

# Create your models here.

# 出版社表
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    # 出版社名字
    name = models.CharField(max_length=12)
    # 出版社会地址
    addr = models.TextField()
    # 成立时间
    date = models.DateField()

    def __str__(self):
        return self.name

# 书籍表
class Book(models.Model):
    # 作者
    title = models.CharField(max_length=12)
    # 价格：最多显示6位，小数位2位
    price = models.DecimalField(max_digits=6,decimal_places=2)
    # ISBN 书籍的唯一编号
    isbn = models.CharField(max_length=20,unique=True)
    # 外键关联出版社
    publisher = models.ForeignKey(to='Publisher',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# 作者表
class Author(models.Model):
    # 姓名
    name = models.CharField(max_length=12)
    # 性别
    gender = models.SmallIntegerField(choices=((1,'男'),(2,'女'),(3,'保密')),default=3)

    # 手机号 唯一约束
    phone = models.CharField(max_length=12,unique=True)
    # 邮箱
    email = models.EmailField()
    # 多对多关联书籍
    book = models.ManyToManyField(to='Book')
    # 一对一，详细信息
    info = models.OneToOneField(to='AuthorInfo')

    def __str__(self):
        return self.name

# 作者详细信息表
class AuthorInfo(models.Model):
    # 生日
    birthday = models.DateTimeField()
    # 住址
    city = models.CharField(max_length=12)
    # 婚否
    is_marry = models.BooleanField()
    # 收入
    income = models.BigIntegerField()