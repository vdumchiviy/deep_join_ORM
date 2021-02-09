from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Name')
    text = models.TextField(verbose_name='Content')
    published_at = models.DateTimeField(verbose_name='Release Date')
    image = models.ImageField(null=True, blank=True,
                              verbose_name='Image',)
    scopes = models.ManyToManyField('Scope', through='ArticleScope')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title


class Scope(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    articles = models.ManyToManyField(Article, through='ArticleScope')

    class Meta:
        verbose_name = "Scope"
        verbose_name_plural = "Scopes"

    def __str__(self):
        return self.name


class ArticleScope(models.Model):

    article = models.ForeignKey(
        Article, verbose_name="Article", on_delete=models.CASCADE)
    scope = models.ForeignKey(
        Scope, verbose_name="Scope", on_delete=models.CASCADE)
    is_favorite = models.BooleanField(verbose_name="Favorite", default=False)

    class Meta:
        verbose_name = "ArticleScope"
        verbose_name_plural = "ArticleScopes"

    def __str__(self):
        return f"Article N{self.article}, scope N{self.scope} is favorite {self.is_favorite}"
