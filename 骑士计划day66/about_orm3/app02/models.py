from django.db import models

# Create your models here.

# 评论表
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=255)
    push_time = models.DateTimeField(auto_now_add=True)
    # 父关联：自关联，一个评论可以没有幅评论所以null=True
    pcomment = models.ForeignKey(to='self',null=True)

    def __str__(self):
        return self.content