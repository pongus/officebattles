from django.contrib import admin

# Register your models here.
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Company name', {'fields': ['name']}),
    ]
    list_filter = ['created', 'updated']
    search_fields = ['name']

admin.site.register(Company, CompanyAdmin)
