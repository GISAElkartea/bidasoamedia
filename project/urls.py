from django.conf.urls.defaults import patterns, include, url
from django.views.generic import RedirectView
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

import oembed
oembed.autodiscover()

from project.sitemaps import sitemaps


urlpatterns = patterns('',
        url(r'^$', RedirectView.as_view(url='articles')),
        url(r'^articles/', include('project.articles.urls', namespace='articles')),
        url(r'^flat/', include('project.flat.urls', namespace='flat')),
        url(r'^grappelli/', include('grappelli.urls')),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^adminfiles/', include('adminfiles.urls')),
        url(r'^markitup/', include('markitup.urls')),
        url(r'^feedback/', include('feedback.urls')),
        url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
