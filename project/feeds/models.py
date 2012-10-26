from django.db import models
from django.core.cache import cache
from django.conf import settings
from django.utils.translation import ugettext as _

from feedparser import parse


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
    def cache_key(self):
        return 'feed-{pk}-{url}'.format(pk=self.pk, url=self.url)

    def parse(self):
        if cache.has_key(self.cache_key):
            return cache.get(self.cache_key)
        else:
            return self.update()
            
    def update(self):
        feed = parse(self.url)
        cache.set(self.cache_key, feed.entries, settings.FEED_CACHE_TIME)
        return feed.entries
