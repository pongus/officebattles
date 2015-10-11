from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User)
    company = models.ForeignKey('companies.Company')
    office = models.ForeignKey('offices.Office')
    games = models.ManyToManyField('games.Game')
