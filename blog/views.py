from django.shortcuts import render

from django.views.generic import DetailView

from .models import Article

# Create your views here.

class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.viewed()
        return obj
