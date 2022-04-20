from django import forms

from .models import Blog


class BlogForm(forms.ModelForm):
    tags = forms.CharField(max_length=200)

    class Meta:
        model = Blog
        fields = ['title', 'description', 'image', 'category']
