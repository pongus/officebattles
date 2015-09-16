from django.contrib import admin

# Register your models here.
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',    {'fields': ['name']}),
        ('Created', {'fields': ['created'], 'classes': ['collapse']}),
    ]
    list_filter = ['created']
    search_fields = ['name']

admin.site.register(Company, CompanyAdmin)
