from django.contrib import admin
from .models import Company, Logo


class CompanyAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name', 'created', 'updated')
    list_filter = ['created', 'updated']
    search_fields = ['name']

admin.site.register(Company, CompanyAdmin)


class LogoAdmin(admin.ModelAdmin):
    fields = ['logo', 'company']
    list_display = ('logo', 'company', 'created', 'updated')
    list_filter = ['created', 'updated']
    search_fields = ['logo']

admin.site.register(Logo, LogoAdmin)
