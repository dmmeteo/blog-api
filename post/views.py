from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin

from models import Post


class PostCreateView(CreateView):
    pass


class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    model = Post

    def get_queryset(self, *args, **kwargs):
        qs = super(PostListView, self).get_queryset(*args, **kwargs).order_by('-timestamp')
        return qs


class PostUpdateView(UpdateView):
    pass


class PostDeleteView(DeleteView):
    pass