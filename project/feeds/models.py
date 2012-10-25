from django.db import models
from django.utils.translation import ugettext as _


class Feed(models.Model):
    class Meta:
        verbose_name = _('Feed')
        verbose_name_plural = _('Feeds')

    url = models.URLField(verbose_name=_('url'))
    quantity = models.PositiveSmallIntegerField(default=5, 
            verbose_name=_('quantity'))

    def __unicode__(self):
        return self.url
