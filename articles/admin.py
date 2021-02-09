from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ArticleScope, Scope

# superuser for admin: admin/1


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        favorite_counter = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data and form.cleaned_data['is_favorite']:
                favorite_counter += 1
        #     # вызовом исключения ValidationError можно указать админке о наличие ошибки
        #     # таким образом объект не будет сохранен,
        #     # а пользователю выведется соответствующее сообщение об ошибке

        if favorite_counter > 1:
            raise ValidationError('Only one of the scopes must be favorite')
        elif favorite_counter == 0:
            raise ValidationError('One of the scopes must be favorite')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
