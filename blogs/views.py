from .models import Blog, Lang, Category, Cookie
from .serializers import BlogSerializer, LangSerializer, CategorySerializer, CookieSerializer
from rest_framework import viewsets, mixins


class BlogViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet, ):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class LangViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, ):
    queryset = Lang.objects.all()
    serializer_class = LangSerializer


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, ):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CoockieViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, ):
    queryset = Cookie.objects.all()
    serializer_class = CookieSerializer
