from django.urls import path
from . import views

urlpatterns = [
    path('', views.tubelist, name='tubelist'),
    path('<int:pk>/', views.tubedetail, name='tubedetail'),
    path('tag/<str:tag>/', views.posttag, name='posttag'),
    path('write/', views.write, name='write'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]