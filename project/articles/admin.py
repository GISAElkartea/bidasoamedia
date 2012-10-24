from django.contrib import admin

from adminfiles.admin import FilePickerAdmin

from project.articles.models import Article, Category


class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(FilePickerAdmin):
    adminfiles_fields = ['description', 'body']
admin.site.register(Article, ArticleAdmin)
