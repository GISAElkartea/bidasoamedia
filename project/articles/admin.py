from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from project.articles.models import Article, Category


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(AdminImageMixin, admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    fields = (('title', 'pub_date'), 'image', 'categories', 'description', 'body')
    filter_horizontal = ('categories',)
    list_display = ('title', 'pub_date')
    list_filter = ('categories', 'pub_date')
    search_fields = ('title', 'description', 'body')
admin.site.register(Article, ArticleAdmin)
