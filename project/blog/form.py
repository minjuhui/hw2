from django import forms
from .models import Blog

# 모델기반 입력공간
class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog 
        fields = ['title', 'body']