from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=128, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @classmethod
    def list(cls):
        return cls.objects.order_by('-updated')


class Logo(models.Model):
    company = models.ForeignKey('companies.Company')
    logo = models.ImageField(upload_to='logos/%Y/%m/%d', height_field=None, width_field=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.logo

    @classmethod
    def latest(cls, company_id):
        return cls.objects.filter(company_id=company_id).order_by('-updated').first()
