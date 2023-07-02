from django.core.management import BaseCommand
import requests
from blogs.models import Blog

url = 'http://62.210.99.231:6666'


def split_paragraphs(text: str):
    try:
        data = {'text': text}
        r = requests.post(url, json=data)
        return (r.text).strip()
    except TypeError as e:
        raise Exception(f"{e} -- param : {text}")


class Command(BaseCommand):
    def handle(self, *args, **options):
        blogs = Blog.objects.filter(is_copyrighted=False, is_processed=True, is_splitted=False).all()
        for blog in blogs:
            print(blog.id)
            new_text = split_paragraphs(blog.content)
            blog.content = new_text
            blog.is_splitted = True
            blog.save()
