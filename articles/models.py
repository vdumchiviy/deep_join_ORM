from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Name')
    text = models.TextField(verbose_name='Content')
    published_at = models.DateTimeField(verbose_name='Release Date')
    image = models.ImageField(null=True, blank=True,
                              verbose_name='Image',)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title


class ArticleScope(models.Model):

    name = models.CharField(max_length=50, verbose_name="Name")
    members = models.ManyToManyField(Article, verbose_name="Member")

    class Meta:
        verbose_name = "Scope"
        verbose_name_plural = "Scopes"

    def __str__(self):
        return self.name
