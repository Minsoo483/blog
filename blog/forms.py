from django import forms

from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'photo']
        labels = {
            'title': '제목',
            'photo': '사진'
        }