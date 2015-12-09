from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=128, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Logo(models.Model):
    company = models.ForeignKey('companies.Company')
    logo = models.ImageField(upload_to='logos/%Y/%m/%d', height_field=None, width_field=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.logo
