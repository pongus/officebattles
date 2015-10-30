from django.db import models
from django.contrib.auth.models import User


class Battle(models.Model):
    game = models.ForeignKey('games.Game')
    players = models.ManyToManyField(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.game)


class Result(models.Model):
    battle = models.ForeignKey('battles.Battle')
    player = models.ForeignKey(User)
    rank = models.PositiveSmallIntegerField(null=True)
    score = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.player) + ', Rank: ' + str(self.rank) + ', Score: ' + str(self.score)
