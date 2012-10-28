from django.contrib import admin

from adminfiles.admin import FilePickerAdmin
from preferences.admin import PreferencesAdmin
from sortable.admin import SortableAdmin

from project.flat.models import ContactPreferences, Flatpage


class ContactPreferencesAdmin(FilePickerAdmin, PreferencesAdmin):
    adminfiles_fields = ['text']
admin.site.register(ContactPreferences, ContactPreferencesAdmin)


class FlatpageAdmin(SortableAdmin, FilePickerAdmin):
    fields = ('title', 'text')
    search_fields = ('title', 'text')
    adminfiles_fields = ('text',)
admin.site.register(Flatpage, FlatpageAdmin)
