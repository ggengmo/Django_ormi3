# book > urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter # default router 기능 많음 , simple router는 기능 적음
from .views import BookViewSet

router = DefaultRouter()
router.register('', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]