from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _
from django.utils.timezone import now

from markitup.fields import MarkupField
from autoslug import AutoSlugField
from sorl.thumbnail import ImageField


class Category(models.Model):
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    name = models.CharField(max_length=25, verbose_name=_('name'))

    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'articles:category', (), {'slug': self.slug}

    @property
    def number(self):
        index = list(Category.objects.values_list('pk', flat=True)).index(
                self.pk)
        return index % settings.CATEGORY_NUMBER

class ArticleManager(models.Manager):
    def published(self):
        q = self.get_queryset()
        return q.filter(pub_date__lte=now())


class Article(models.Model):
    objects = ArticleManager()
    class Meta:
        ordering = ('-pub_date',)
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    title = models.CharField(max_length=100, verbose_name=_('title'))
    description = MarkupField(blank=True, verbose_name=_('description'),
            help_text=_('populated from body if not given'))
    body = MarkupField(verbose_name=_('body'))
    image = ImageField(blank=True, upload_to='images',
            verbose_name=_('image'))

    pub_date = models.DateTimeField(default=now,
            verbose_name=_('publication date'))
    categories = models.ManyToManyField(Category, blank=True,
            verbose_name=_('categories'))
    slug = AutoSlugField(populate_from='title', unique=True)

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'articles:detail', (), {'slug': self.slug}
