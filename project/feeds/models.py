from django.db import models
from django.core.cache import cache
from django.utils.translation import ugettext as _

from feedparser import parse
from purl import URL


class Feed(models.Model):
    class Meta:
        verbose_name = _('Feed')
        verbose_name_plural = _('Feeds')

    url = models.URLField(verbose_name=_('url'))
    quantity = models.PositiveSmallIntegerField(default=5, 
            verbose_name=_('quantity'))

    def __unicode__(self):
        return self.url

    @property
    def favicon(self):
        return URL(self.url).path('favicon.ico').as_string()

    @property
    def cache_key(self):
        return 'feed-{pk}-{url}'.format(pk=self.pk, url=self.url)

    def parse(self):
        if cache.has_key(self.cache_key):
            return cache.get(self.cache_key)
        else:
            return self.update()
            
    def update(self):
        feed = parse(self.url)
        entries = feed.entries[:self.quantity]
        cache.set(self.cache_key, entries)
        return entries
