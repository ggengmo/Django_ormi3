# notice/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.notice, name="notice"),
    path("free/", views.free, name="free"),
    path("free/<int:pk>/", views.free_detail, name="free_detail"),
    path("onenone/", views.onenone, name="onenone"),
    path("onenone/<int:pk>/", views.onenone_detail, name="onenone_detail"),
]
