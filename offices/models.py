from django.db import models


class Office(models.Model):
    company = models.ForeignKey('companies.Company')
    name = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @classmethod
    def list(cls, company_id):
        return cls.objects.filter(company_id=company_id).order_by('-updated')
