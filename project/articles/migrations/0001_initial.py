# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 21:52
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.utils.timezone
import markitup.fields
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', markitup.fields.MarkupField(blank=True, help_text='populated from body if not given', no_rendered_field=True, verbose_name='description')),
                ('body', markitup.fields.MarkupField(no_rendered_field=True, verbose_name='body')),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, upload_to=b'images', verbose_name='image')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='publication date')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=b'title', unique=True)),
                ('_body_rendered', models.TextField(blank=True, editable=False)),
                ('_description_rendered', models.TextField(blank=True, editable=False)),
            ],
            options={
                'ordering': ('-pub_date',),
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='izena')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=b'name', unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(blank=True, to='articles.Category', verbose_name='categories'),
        ),
    ]