from django.contrib import admin
from .models import Office


class OfficeAdmin(admin.ModelAdmin):
    fields = ['company', 'name']
    list_display = ('name', 'company', 'created', 'updated')
    list_filter = ['company', 'created', 'updated']
    search_fields = ['name']

admin.site.register(Office, OfficeAdmin)
