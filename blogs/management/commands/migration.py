from django.core.management import BaseCommand
from blogs.models import Lang


class Command(BaseCommand):
    def handle(self, *args, **options):
        langs = ["fr", "en", "es", "du"]
        for l in langs:
            if not Lang.objects.filter(l).exists():
                Lang.objects.create(name=l)
