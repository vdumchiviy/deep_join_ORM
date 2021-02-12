from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Scope, ArticleScope


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all().prefetch_related('scopes')
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
    context = {'object_list': articles}

    return render(request, template, context)
