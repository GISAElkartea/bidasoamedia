from django.conf.urls.defaults import patterns, url

from project.articles.views import ArticleList#, ArticleDetail, CategoryDetail


urlpatterns = patterns('',
        url('^$', ArticleList.as_view(), name='list'),
)
