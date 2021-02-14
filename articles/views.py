from django.views.generic import ListView
from django.shortcuts import render
from django.db.models import OuterRef, Subquery, Prefetch
from articles.models import Article, Scope, ArticleScope


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles = Article.objects.all().prefetch_related(
        'scope_relations').order_by(ordering)
    # articles = Article.objects.all().prefetch_related(
    #     'scope_relations').order_by(ordering)
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    context = {'object_list': articles}

    return render(request, template, context)
