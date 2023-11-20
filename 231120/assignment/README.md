# 1. 프로젝트 설정
## 폴더 생성 및 이동
mkdir assignment

cd assignment

## 가상환경 및 Django 설치
python -m venv venv

pip install django

## 프로젝트 및 앱 생성
django-admin startproject project .

python manage.py startapp blog
python manage.py startapp notice

## project > settings.py
INSTALLED_APPS = [
    '''
    생략
    '''
    "django.contrib.staticfiles",
    'rest_framework',
    'blog',
    'notice',
]
'''
생략
'''
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

## project > urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('blog/', include('blog.urls')),
    path('notice/', include('notice.urls')),
]


# 2. Blog app
## Blog 모델 생성
### blog > models.py

from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

## DB 적용
python manage.py makemigrations
python manage.py migrate

## blog > serializers.py
from rest_framework.serializers import ModelSerializer
from .models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

## blog > views.py
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

## blog > urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

## 슈퍼유저 생성
### python manage.py createsuperuser
사용자 이름 (leave blank to use 'rudah'): rudah
이메일 주소: rudah365dlf@gmail.com
Password: 
Password (again):

## 테스트
[
    {
        "id": 1,
        "title": "test1",
        "content": "11",
        "created_at": "2023-11-20T15:28:45.764011",
        "updated_at": "2023-11-20T15:28:45.764011",
        "author": 1
    },
    {
        "id": 2,
        "title": "test2",
        "content": "22",
        "created_at": "2023-11-20T15:28:49.657072",
        "updated_at": "2023-11-20T15:28:49.657072",
        "author": 1
    },
    {
        "id": 3,
        "title": "test3",
        "content": "33",
        "created_at": "2023-11-20T15:28:53.689096",
        "updated_at": "2023-11-20T15:28:53.689096",
        "author": 1
    }
]

9개 작성

## 인증 구현
## blog > permissions.py

from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated
        
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


## blog > views.py
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]

/blog: 회원인 사람만 R, C 가능
/blog/int:post_pk: 회원인 사람만 R, 작성자만 UD 가능

기능 테스트

# 3. Notice App
## Notice 모델 생성
### notice > models.py
from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

## DB 적용
python manage.py makemigrations
SystemCheckError: System check identified some issues:

ERRORS:
blog.Post.author: (fields.E304) Reverse accessor 'User.post_set' for 'blog.Post.author' clashes with reverse accessor for 'notice.Post.author'.
        HINT: Add or change a related_name argument to the definition for 'blog.Post.author' or 'notice.Post.author'.
notice.Post.author: (fields.E304) Reverse accessor 'User.post_set' for 'notice.Post.author' clashes with reverse accessor for 'blog.Post.author'.
        HINT: Add or change a related_name argument to the definition for 'notice.Post.author' or 'blog.Post.author'.

## 에러 발생하여 blog, notice modle 수정
### notice > models.py

from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notice_author')
    '''
    생략
    '''
# blog > models.py

from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_author')
    '''
    생략
    '''

python manage.py makemigrations
python manage.py migrate

# notice > serializers.py
from rest_framework.serializers import ModelSerializer
from .models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

## 테스트
blog와 같이 글 9개 작성 후 
/notice: 회원이 아닌 사람도 R 가능, 회원인 사람만 C 가능
/notice/int:post_pk: 회원이 아닌 사람도 R 가능, 작성자만 UD 가능

기능 테스트

## 인증 구현
# notice > permissions.py
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated
        
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
        
# notice > views.py
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
