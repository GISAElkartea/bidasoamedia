from django.contrib import admin

from project.feeds.models import Feed


class FeedAdmin(admin.ModelAdmin):
    search_fields = ('url',)
    fields = (('url', 'quantity'),)
    list_display = ('url', 'quantity')
admin.site.register(Feed, FeedAdmin)
