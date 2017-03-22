from django.contrib import admin

from preferences.admin import PreferencesAdmin

from project.flat.models import ContactPreferences, Flatpage


class ContactPreferencesAdmin(PreferencesAdmin, admin.ModelAdmin):
    pass
admin.site.register(ContactPreferences, ContactPreferencesAdmin)


class FlatpageAdmin(admin.ModelAdmin):
    fields = ('title', 'text')
    search_fields = ('title', 'text')
    pass
admin.site.register(Flatpage, FlatpageAdmin)
