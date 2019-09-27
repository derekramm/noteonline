from django.db import models

# Create your models here.
from django.utils import timezone


class Author(models.Model):
    username = models.CharField(verbose_name='账户', max_length=200)
    password = models.CharField(verbose_name='密码', max_length=200)
    email = models.EmailField(verbose_name='邮箱')
    poster = models.ImageField(verbose_name='头像', upload_to='images/authos/')

    def __str__(self): return self.username


class Article(models.Model):
    title = models.CharField(verbose_name='标题', max_length=200)
    content = models.TextField(verbose_name='内容')
    summary = models.TextField(verbose_name='摘要')
    created_at = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='修改时间', default=timezone.now)
    author = models.ForeignKey(verbose_name='作者', to=Author, on_delete=models.CASCADE)
    topics = models.CharField(verbose_name='类别', max_length=200)
    tags = models.CharField(verbose_name='标签', max_length=200)

    def __str__(self): return self.title

class Comment(models.Model):
    text = models.TextField(verbose_name='内容')
    prop = models.CharField(verbose_name='属性词', max_length=200)
    adj = models.CharField(verbose_name='形容词', max_length=200)
    sentiment = models.IntegerField(verbose_name='情感', default=1)  # 0表示消极，1表示中性，2表示积极
    begin_pos = models.IntegerField(verbose_name='开始位置', default=-1)
    end_pos = models.IntegerField(verbose_name='结束位置', default=-1)
    abstract = models.TextField(verbose_name='摘要')
    article = models.ForeignKey(verbose_name='文章', to=Article, on_delete=models.CASCADE)
