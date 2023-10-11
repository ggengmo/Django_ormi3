# memo > models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    main_image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        time = self.created_at.strftime('%Y-%m-%d %H:%M')
        return f'제목: {self.title}, 작성일: {time}'
    