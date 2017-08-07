from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    
    # TODO remove all or do something better
    url(settings.ADMIN_URL, include(admin.site.urls)),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^post/', include('post.urls', namespace='post')),
    # url(r'^article/', include(article_urls)),
    url(r'^category/', include('category.urls', namespace='category')),
    # url(r'^dashboard/', include('dashboard_urls')),
    
    # API
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DJANGO_USE_DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
