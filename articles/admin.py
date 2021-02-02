from django.contrib import admin

from .models import Article, ArticleScope

# superuser for admin: admin/1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(ArticleScope)
class ArticleScopeAdmin(admin.ModelAdmin):
    pass
