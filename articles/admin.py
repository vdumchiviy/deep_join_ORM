from django.contrib import admin

from .models import Article, ArticleScope

# superuser for admin: admin/1


# @admin.register(ArticleScope)
class ArticleScopInline(admin.StackedInline):
    model = ArticleScope.members.through



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopInline]

