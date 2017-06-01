from django import forms
# from django.forms import ModelForm, Textarea, TextInput
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

    def clean_title(self):  # TODO normal clean to validate updated data
        title = self.cleaned_data['title']
        slug = slugify(title)
        try:
            # TODO us a Post.objects.get(pk) and than slug
            Post.objects.get(slug=slug)
            raise forms.ValidationErorr('Title already exist. Please try different one.')
        except Post.DoesNotExist:
            return title
        except:
            raise forms.ValidationError('Title already exist. Please try different one.')