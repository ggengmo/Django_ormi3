from django import forms
from .models import Post


class Notice_PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'