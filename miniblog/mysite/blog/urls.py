# blog > urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('register/', views.userregister, name='userregister'),
    path('login/', views.userlogin, name='userlogin'),
]