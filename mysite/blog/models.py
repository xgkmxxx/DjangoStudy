# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models



# Create your models here.

class Category(models.Model):
    """
    分类
    """
    name = models.CharField('名称',max_length=16)

class Tag(models.Model):
    """
    标签
    """

    name = models.CharField('名称', max_length=16)

class BlogsPost(models.Model):
    """
    博客
    """
    title = models.CharField('标题',max_length=150)
    author = models.CharField('作者', max_length=16)
    body = models.TextField('正文')
    timestamp = models.DateTimeField('发布时间', auto_now_add=True)
    category = models.ForeignKey(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')


class Comment(models.Model):
    """
    评论
    """

    blog = models.ForeignKey(BlogsPost, verbose_name='博客')

    name = models.CharField('称呼', max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容', max_length=140)

    timestamp = models.DateTimeField('发布时间', auto_now_add=True)
