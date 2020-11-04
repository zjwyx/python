from django.db import models

# Create your models here.

class MyClass(models.Model):
    cname = models.CharField(max_length=12)

    def __str__(self):
        return self.cname

class Student(models.Model):
    sname = models.CharField(max_length=12)
    mycalss = models.ForeignKey(to='MyClass')

    def __str__(self):
        return self.sname

class Teacher(models.Model):
    tname = models.CharField(max_length=12)
    myclass = models.ManyToManyField(to='MyClass')

    def __str__(self):
        return self.tname
