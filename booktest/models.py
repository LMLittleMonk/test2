from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)#书名

    bpub_date = models.DateField()#出版时间

    bread = models.IntegerField(default=0)#阅读数

    bcomment = models.IntegerField(default=0)#评论量

    isDelete = models.BooleanField(default=False)#逻辑删除

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)

    hgender = models.BooleanField(default=True)#性别默认男性

    isDelete = models.BooleanField(default=False)#逻辑删除

    hcomment = models.CharField(max_length=200)#英雄描述

    hbook = models.ForeignKey('BookInfo')