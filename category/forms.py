from django import forms
from models import Category


class CategoryForm(forms.ModelForm):
    error_css_class = 'has-danger'

    class Meta:
        model = Category
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                             'cols': 40,
                                             'rows': 20})
        }


