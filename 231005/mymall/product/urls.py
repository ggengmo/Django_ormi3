# product/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name='product'),
    path('<int:pk>/', views.post, name='post'),
]