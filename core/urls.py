from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),

    url(r'', include('base.urls', namespace='base')),
    url(r'^post/', include('post.urls', namespace='post')),
    # url(r'^article/', include(article_urls)),
    url(r'^category/', include('category.urls', namespace='category')),
    # url(r'^dashboard/', include('dashboard_urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


