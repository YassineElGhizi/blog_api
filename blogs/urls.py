from django.urls import path, include
from rest_framework import routers
from .views import BlogViewSet, CategoryViewSet, LangViewSet, CoockieViewSet

router = routers.DefaultRouter()
router.register('blogs', BlogViewSet)
router.register('categories', CategoryViewSet)
router.register('Languages', LangViewSet)
router.register('cookies', CoockieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
