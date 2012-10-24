from django.db import models
from django.utils.translation import ugettext as _
from django.utils.timezone import now

from markitup.fields import MarkupField
from autoslug import AutoSlugField


class Category(models.Model):
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    name = models.CharField(max_length=25, verbose_name=_('name'))

    slug = AutoSlugField(populate_from='name', unique=True)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    class Meta:
        ordering = ('-pub_date',)
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    title = models.CharField(max_length=100, verbose_name=_('title'))
    description = MarkupField(blank=True, verbose_name=_('description'), 
            help_text=_('populated from body if not given'))
    body = MarkupField(verbose_name=_('body'))

    pub_date = models.DateTimeField(default=now,
            verbose_name=_('publication date'))
    categories = models.ManyToManyField(Category, blank=True, null=True,
            verbose_name=_('categories'))
    slug = AutoSlugField(populate_from='title', unique=True)

    def __unicode__(self):
        return self.title
