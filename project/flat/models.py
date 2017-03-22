from django.db import models
from django.utils.translation import ugettext as _

from preferences.models import Preferences
from markitup.fields import MarkupField
from autoslug import AutoSlugField


class ContactPreferences(Preferences):
    class Meta:
        verbose_name = _('Contact Preferences')
        verbose_name_plural = _('Contact Preferences')

    __module__ = 'preferences.models'
    text = MarkupField(verbose_name=_('text'))
    email = models.EmailField(verbose_name=_('email'))


class Flatpage(models.Model):
    class Meta:
        verbose_name = _('flatpage')
        verbose_name_plural = _('flatpages')

    title = models.CharField(max_length=50, verbose_name=_('title'))
    text = MarkupField(verbose_name=_('text'))

    slug = AutoSlugField(populate_from='title', unique=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'flat:detail', (), {'slug': self.slug}
