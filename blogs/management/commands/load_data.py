from django.core.management import BaseCommand
from blogs.models import Lang, Blog, Category
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        data_json_file = "/home/smarteez/PycharmProjects/adnanE/blogs.json"
        with open(data_json_file, mode='r', encoding='utf-8') as f:
            data = json.load(f)
        fr = Lang.objects.filter(name__iexact="fr").first()
        cat = Category.objects.filter(name__iexact="Health").first()

        for item in data:
            if Blog.objects.filter(h1__exact=item.get("h2")).exists():
                continue
            Blog.objects.create(title_seo=item.get("title"), description_seo=item.get("description"), h1=item.get("h1"),
                                h2=item.get("h2"), content=item.get("content"), image=item.get("img"), language=fr,
                                href=item.get("link"), categorie=cat)
