from django.contrib import admin

# Register your models here.
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name', 'created', 'updated')
    list_filter = ['created', 'updated']
    search_fields = ['name']

admin.site.register(Company, CompanyAdmin)
