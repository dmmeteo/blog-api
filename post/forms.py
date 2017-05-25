from django.forms import ModelForm, Textarea, TextInput
from models import Post


class PostForm(ModelForm):
    error_css_class = 'has-danger'

    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'content': Textarea(attrs={'class': 'form-control',
                                       'cols': 80,
                                       'rows': 20})
        }
