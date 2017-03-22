from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from django.contrib import admin
admin.autodiscover()

from project.sitemaps import sitemaps
from project.articles.feeds import ArticlesRSS, ArticlesAtom


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='articles')),
    url(r'^articles/', include('project.articles.urls', namespace='articles')),
    url(r'^rss/articles/$', ArticlesRSS(), name='rss'),
    url(r'^atom/articles/$', ArticlesAtom(), name='atom'),
    url(r'^flat/', include('project.flat.urls', namespace='flat')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
