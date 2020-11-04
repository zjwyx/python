from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=12)
    books = models.ManyToManyField(to='Book')

    def __str__(self):
        return self.name