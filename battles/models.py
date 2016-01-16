from django.db import models
from django.contrib.auth.models import User


class Battle(models.Model):
    game = models.ForeignKey('games.Game')
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.game.name

    @classmethod
    def including_related_results(cls):
        return cls.objects.prefetch_related('result_set').filter(completed=True).order_by('-created')


class Result(models.Model):
    battle = models.ForeignKey(Battle)
    player = models.ForeignKey(User)
    score = models.IntegerField(null=True)
    is_home = models.NullBooleanField()
    has_coin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
