# blog > ulrs.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.postlist, name='postlist'),
]