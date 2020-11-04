from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title



class Author(models.Model):
    name = models.CharField(max_length=12)
    books = models.ManyToManyField(to='Book',through='Author2Book',through_fields=('author','book'))

    def __str__(self):
        return self.name


class Author2Book(models.Model):
    author = models.ForeignKey(to='Author')
    book = models.ForeignKey(to='Book')
    score= models.IntegerField()

    def __str__(self):
        return self.score

    class Meta:
        unique_together = (('author','book'),)


# Author2Book.objects.create(author_id=1,book_id=2,score=200)