from django.views.generic.base import TemplateView


class BaseHomeView(TemplateView):
    template_name = 'base/home.html'
