from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    company = models.ForeignKey('companies.Company')
    office = models.ForeignKey('offices.Office')
    games = models.ManyToManyField('games.Game')
