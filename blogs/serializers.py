from rest_framework import serializers
from .models import Blog, Lang, Category, Cookie


class BlogSerializer(serializers.ModelSerializer):
    language = serializers.CharField(write_only=True, required=True)
    categorie = serializers.CharField(write_only=True, required=True)
    content = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Blog
        fields = ["title_seo", "description_seo", "h1", "h2", "content", "image", "language", "href", "categorie"]

    def validate_language(self, value):
        if not Lang.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError(f'There is no Language with name = {value}')
        return value

    def validate_h1(self, value):
        if Blog.objects.filter(h1__iexact=value).exists():
            raise serializers.ValidationError(f'A blog with h1 = {value}, Already Exist')
        return value

    def create(self, validated_data):
        category, created = Category.objects.get_or_create(name=validated_data.get("categorie"))
        lang = Lang.objects.filter(name__iexact=validated_data.get("language")).first()
        b = Blog.objects.create(title_seo=validated_data.get("title_seo"), h1=validated_data.get("h1"),
                                description_seo=validated_data.get("description_seo"), language=lang,
                                categorie=category, h2=validated_data.get("h2"), content=validated_data.get("content"),
                                image=validated_data.get("image"), href=validated_data.get("href"))
        return b


class LangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lang
        fields = ["name", ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", ]


class CookieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookie
        fields = ["token", "name", ]
