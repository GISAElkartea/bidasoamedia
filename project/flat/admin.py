from django.contrib import admin

from preferences.admin import PreferencesAdmin

from project.flat.models import Flatpage


class FlatpageAdmin(admin.ModelAdmin):
    fields = ('title', 'text')
    search_fields = ('title', 'text')
    pass
admin.site.register(Flatpage, FlatpageAdmin)
