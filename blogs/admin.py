from django.contrib import admin
from .models import Lang, Category, Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = (
        "id", "h1", "categorie", "is_ready", "is_processed", "is_copyrighted", "language", "is_published", "created_at")
    list_filter = ("is_ready", "is_published", "is_processed", "is_copyrighted", "created_at", "categorie", "language",)
    readonly_fields = (
        "is_ready", "is_processed", "is_copyrighted", "social_media", "is_reeled", "image", "href", "parent_id")
    list_per_page = 10


@admin.register(Lang)
class LangAdmin(admin.ModelAdmin):
    model = Lang
    list_display = ("id", "name", "deepl_lang")


admin.site.register(Category)
