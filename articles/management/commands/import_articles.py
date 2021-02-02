import json

from django.core.management.base import BaseCommand
from articles.models import Article


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('articles.json', 'r') as import_files:

            reader = json.load(import_files)

            for article in reader:
                fields = article["fields"]
                created = Article(id=article["pk"],
                                  title=fields["title"],
                                  text=fields["text"],
                                  published_at=fields["published_at"],
                                  image=fields["image"]
                                  )
                created.save()
