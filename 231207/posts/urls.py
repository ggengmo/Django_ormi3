# posts > urls.py

from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    CommentCreateView,
    CommentListView,
    LikeView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'), # 게시물 리스트
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'), # 게시물 상세보기
    path('write/', PostCreateView.as_view(), name='post_create'), # 게시물 생성
    path('comments/', CommentCreateView.as_view(), name='comment_create'), # 댓글 생성
    path('<int:post_id>/comments/', CommentListView.as_view(), name='comment_list'), # 댓글 리스트
    path('<int:post_id>/like/', LikeView.as_view(), name='post_like'), # 게시물에 대한 좋아요
]
