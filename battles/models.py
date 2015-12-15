from django.db import models
from django.contrib.auth.models import User


class Battle(models.Model):
    game = models.ForeignKey('games.Game')
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Result(models.Model):
    battle = models.ForeignKey('battles.Battle')
    player = models.ForeignKey(User)
    score = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
