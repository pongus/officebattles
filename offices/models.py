from django.db import models

# Create your models here.
class Office(models.Model):
    company = models.ForeignKey('companies.Company')
    name = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
