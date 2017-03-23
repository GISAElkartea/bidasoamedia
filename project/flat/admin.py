from django.contrib import admin

from project.flat.models import Flatpage


class FlatpageAdmin(admin.ModelAdmin):
    fields = ('title', 'text')
    search_fields = ('title', 'text')
    pass
admin.site.register(Flatpage, FlatpageAdmin)
