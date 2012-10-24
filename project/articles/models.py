from django.db import models
from django.utils.translation import ugettext as _

from markitup.fields import MarkupField
from autoslug import AutoSlugField


class Article(models.Model):
    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    title = models.CharField(max_length=100, verbose_name=_('title'))
    description = MarkupField(blank=True, verbose_name=_('description'))
    body = MarkupField(verbose_name=_('body'))

    slug = AutoSlugField(populate_from='title', unique=True)

    def __unicode__(self):
        return self.title
