#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from . import views
from django.urls import re_path

app_name = 'blog'

urlpatterns = [
    # 展示文章详情, 直接用通用视图编写
    re_path(r'^article/(?P<pk>\d+)/$', views.ArticleDetailView.as_view(), name='article_detail')

]