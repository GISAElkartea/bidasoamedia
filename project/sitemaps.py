from django.contrib.sitemaps import GenericSitemap

from project.articles.models import Article
from project.flat.models import Flatpage

sitemaps = {
        'articles': ({
            'queryset': Article.objects.published(), 
            'date_field': 'pub_date'
            }, 1),
        'flat pages': ({
            'queryset': Flatpage.objects.all(),
            }, .5),
        }
sitemaps = { name: GenericSitemap(*args) for (name, args) in sitemaps.items() }
