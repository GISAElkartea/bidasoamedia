from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.utils.translation import ugettext_lazy as _

from project.articles.models import Article


class ArticlesRSS(Feed):
    title = _('bidasoamedia.info articles')
    link = '/'
    description = _('Latest updates on bidasoamedia.info articles.')
    author_name = 'bidasoamedia.info'

    def items(self):
        return Article.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return item.get_absolute_url()

    def item_pubdate(self, item):
        return item.pub_date

    def item_categories(self, item):
        return item.categories.iterator()


class ArticlesAtom(ArticlesRSS):
    feed_type = Atom1Feed
    subtitle = ArticlesRSS.description
