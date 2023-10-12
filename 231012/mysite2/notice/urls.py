from django.urls import path
from . import views

urlpatterns = [
    path('', views.notice, name='notice'),
    path('<int:pk>/', views.post, name='post'),
]