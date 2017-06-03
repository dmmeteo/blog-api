from django import forms
from models import Post
from django.utils.text import slugify


class PostForm(forms.ModelForm):
    error_css_class = 'has-danger'

    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control',
                                             'cols': 80,
                                             'rows': 20})
        }


