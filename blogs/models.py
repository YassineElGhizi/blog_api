from django.db import models


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Lang(TimeStamp):
    name = models.CharField(max_length=10)
    deepl_lang = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Category(TimeStamp):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class SocialMedia(TimeStamp):
    credentials = models.TextField(help_text="json format")
    platform = models.CharField(max_length=70)
    page = models.CharField(max_length=70, null=True, blank=True)
    is_baned = models.BooleanField(default=False)


class Blog(TimeStamp):
    title_seo = models.CharField(max_length=100)
    description_seo = models.CharField(max_length=400, null=True, blank=True)
    h1 = models.CharField(max_length=120, db_index=True)
    h2 = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField()
    image = models.TextField(null=True, blank=True)
    alt = models.TextField(null=True, blank=True)
    language = models.ForeignKey(Lang, on_delete=models.CASCADE)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, default=None)
    href = models.TextField(null=True, blank=True)
    is_ready = models.BooleanField(default=False)
    is_processed = models.BooleanField(default=False)
    is_copyrighted = models.BooleanField(default=False)
    categorie = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, default=None)
    social_media = models.ManyToManyField(SocialMedia)
    is_reeled = models.BooleanField(default=False)
    reel_path = models.TextField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    translated_at = models.DateTimeField(null=True, blank=True)
    checked_for_copyright = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.h1}'
