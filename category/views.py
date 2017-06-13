from django.views.generic import (CreateView, ListView, DetailView, UpdateView, DeleteView)
from braces.views import LoginRequiredMixin
from models import Category
from forms import CategoryForm
from django.core.urlresolvers import reverse


class CategoryCreateView(LoginRequiredMixin, CreateView):
    form_class = CategoryForm
    template_name = 'category/category_form.html'
    success_message = '%(title)s is created!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        valid_form = super(CategoryCreateView, self).form_valid(form)
        return valid_form

    def get_success_url(self):
        return reverse('category:list')


class CategoryListView(ListView):
    model = Category

    def get_queryset(self, *args, **kwargs):
        qs = super(CategoryListView, self).get_queryset(*args, **kwargs).order_by('title')
        return qs


class CategoryDetailView(DetailView):
    model = Category


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    pass


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    pass

