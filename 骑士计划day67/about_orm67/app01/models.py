from django.db import models

# Create your models here.

class Publisher(models.Model):
    pname = models.CharField(max_length=12)
    addr = models.TextField()
    birth_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.pname

class Book(models.Model):
    title = models.CharField(max_length=12)
    pric = models.DecimalField(max_digits=6,decimal_places=2)
    # 收藏数
    fav_num = models.PositiveIntegerField()
    # 卖出数
    sale_num = models.PositiveIntegerField()
    publisher = models.ForeignKey(to='Publisher',null=True)

    def __str__(self):
        return self.title