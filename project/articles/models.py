from django.db import models
from django.utils.translation import ugettext as _

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
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    title = models.CharField(max_length=100, verbose_name=_('title'))
    description = MarkupField(blank=True, verbose_name=_('description'))
    body = MarkupField(verbose_name=_('body'))

    pub_date = models.DateTimeField(auto_now_add=True,
            verbose_name=_('publication date'))
    category = models.ManyToManyField(Category, blank=True, null=True,
            verbose_name=_('category'))
    slug = AutoSlugField(populate_from='title', unique=True)

    def __unicode__(self):
        return self.title
