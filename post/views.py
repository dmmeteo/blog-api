from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from models import Post
from forms import PostForm


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = PostForm
    template_name = 'post/post_form.html'
    success_message = '%(title)s is created at %(created_at)s'

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        valid_form = super(PostCreateView, self).form_valid(form)
        return valid_form

    def get_success_url(self):
        return reverse('post:list')

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


class PostUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_form.html'
    success_message = '%(title)s is updated'

    def form_valid(self, form):
        form.instance.last_edit_by = self.request.user
        form_valid = super(PostUpdateView, self).form_valid(form)
        return form_valid

    def get_success_url(self):
        return reverse('post:detail', args=[self.object.slug])  # or kwargs={'pk': self.object.pk}

    def get_context_data(self, *args, **kwargs):
        context = super(PostUpdateView, self).get_context_data(*args, **kwargs)
        context['btn_url'] = self.get_success_url()
        return context


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_message = '%(title)s is deleted'

    def get_success_url(self):
        return reverse('post:list')
