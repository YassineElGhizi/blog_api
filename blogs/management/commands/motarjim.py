from django.core.management import BaseCommand
import requests
import base64
from blogs.models import Blog, Lang

url = 'http://e6fc-62-210-99-231.ngrok-free.app/'


def translate(src: str, dis: str, text: str):
    try:
        encoded = base64.b64encode(bytes(text, 'utf-8'))
        encodedStr = encoded.decode('utf-8')
        contents = {"source": "French", "dest": "English", "version": "Free", "text": encodedStr}
        r = requests.post(url, json=contents)
        if r.status_code == 200:
            decoded = base64.b64decode(bytes(r.text, 'utf-8'))
            return decoded.decode('utf-8')
        else:
            raise Exception(f"Translated returned status code = {r.status_code}")
    except Exception as e:
        return r.text
        # raise Exception(f"{e} -- param : {text}")


class Command(BaseCommand):
    def handle(self, *args, **options):
        bulk_blogs = []
        try:
            blogs = Blog.objects.filter(parent_id__isnull=True).all()
            target_language = Lang.objects.filter(name__iexact="en").first()
            h2, alt = None, None

            for blog in blogs:
                if Blog.objects.filter(parent_id=blog).exists():
                    continue
                print(f"id = {blog.id}")
                src = blog.language.deepl_lang
                translated_content = translate(src, target_language.deepl_lang, blog.content)
                title_seo = translate(src, target_language.deepl_lang, blog.title_seo)
                description_seo = translate(src, target_language.deepl_lang, blog.description_seo)
                h1 = translate(src, target_language.deepl_lang, blog.h1)

                if blog.alt is not None:
                    alt = translate(src, target_language, blog.alt)

                if blog.h2 is not None:
                    if blog.h2 != None:
                        h2 = translate(src, target_language.deepl_lang, blog.h2)

                bulk_blogs.append(Blog(title_seo=title_seo, description_seo=description_seo, h1=h1, h2=h2,
                                       content=translated_content, image=blog.image, alt=alt, language=target_language,
                                       parent_id=blog, categorie=blog.categorie))

            Blog.objects.bulk_create(bulk_blogs)
        except Exception as e:
            Blog.objects.bulk_create(bulk_blogs)
