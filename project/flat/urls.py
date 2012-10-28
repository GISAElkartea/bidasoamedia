from django.conf.urls.defaults import patterns, url

from project.flat.views import FlatpageDetail


urlpatterns = patterns('',
        url('^flatpage/(?P<slug>(\w|\d|-)+)/$', FlatpageDetail.as_view(), name='detail'),
        )
