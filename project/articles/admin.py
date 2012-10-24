from django.contrib import admin

from adminfiles.admin import FilePickerAdmin

from project.articles.models import Article


class ArticleAdmin(FilePickerAdmin):
    adminfiles_fields = ['description', 'body']
admin.site.register(Article, ArticleAdmin)
