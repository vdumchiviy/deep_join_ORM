from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Scope, ArticleScope


def articles_list(request):
    template = 'articles/news.html'
    articles_list = Article.objects.all()
    context = {}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
    context['object_list'] = ['1', '2', '3']
    return render(request, template, context)
