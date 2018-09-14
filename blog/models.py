from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.
"""以博客文章为例统计页面浏览次数练习"""

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发表'),
    )

    title = models.CharField('标题', max_length=200, unique=True)
    slug = models.SlugField('slug', max_length=60) # 用于生成效用的URL
    body = models.TextField('正文')
    pub_date = models.DateTimeField('发布时间', default=now, null=True)
    create_date = models.DateTimeField('创建时间', auto_now_add=True)
    mod_date = models.DateTimeField('修改时间', auto_now=True)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES, default='d')
    views = models.PositiveIntegerField('浏览量', default=0)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    category = models.ForeignKey('Category', verbose_name='分类', on_delete=models.CASCADE
                                 , blank=True, null=True)
    tags = models.ForeignKey('Tags', verbose_name='标签', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[str(self.id)])

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])

class Category(models.Model):
    name = models.CharField('名称', max_length=50)
    def __str__(self):
        return  self.name
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

class Tags(models.Model):
    name = models.CharField('名称', max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
