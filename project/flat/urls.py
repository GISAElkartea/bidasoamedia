from django.conf.urls import url

from project.flat.views import FlatpageDetail


urlpatterns = [
        url('^flatpage/(?P<slug>(\w|\d|-)+)/$', FlatpageDetail.as_view(), name='detail'),
]
