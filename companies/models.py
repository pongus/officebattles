from django.db import models

import datetime
from django.utils import timezone

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField('Created', default=timezone.now)
    updated = models.DateTimeField('Updated', default=timezone.now)
