from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
from django.contrib.messages.views import SuccessMessageMixin

from models import Post
from forms import PostForm


class PostCreateView(SuccessMessageMixin, CreateView):
    form_class = PostForm
    template_name = 'post/post_form.html'
    success_message = '%(title)s is created at %(created_at)s'

    def get_success_url(self):
        return reverse('post_list')

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            created_at=self.object.timestamp
        )


class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    model = Post

    def get_queryset(self, *args, **kwargs):
        qs = super(PostListView, self).get_queryset(*args, **kwargs).order_by('-timestamp')
        return qs


class PostUpdateView(SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_form.html'
    success_message = '%(title)s is updated'

    def get_success_url(self):
        return reverse('post_list')


class PostDeleteView(DeleteView):
    pass
