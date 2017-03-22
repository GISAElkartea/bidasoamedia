from django.conf.urls import url

from project.articles.views import ArticleList, ArticleDetail, ArticleCategory


urlpatterns = [
        url('^$', ArticleList.as_view(), name='list'),
        url('^category/(?P<slug>(\w|\d|-)+)/$', ArticleCategory.as_view(),
            name='category'),
        url('^article/(?P<slug>(\w|\d|-)+)/$', ArticleDetail.as_view(),
            name='detail'),
]
