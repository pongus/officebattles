from django.db import models


GAME_MODES = (
    (0, '1V1'),
    (1, '2V2'),
    (2, '3V3'),
    (3, '4V4'),
    (4, '5V5'),
    (5, 'FFA'),
)


class Game(models.Model):
    office = models.ForeignKey('offices.Office')
    name = models.CharField(max_length=128)
    mode = models.PositiveSmallIntegerField(choices=GAME_MODES, default=0)
    min_players = models.PositiveSmallIntegerField(null=True, blank=True, help_text="If game mode 'Free For All' is selected.")
    max_players = models.PositiveSmallIntegerField(null=True, blank=True, help_text="If game mode 'Free For All' is selected.")
    has_best_of = models.BooleanField(default=False, help_text="Enable best of to make it easier to setup a round of battles.")
    has_coin_toss = models.BooleanField(default=False, help_text="Enable coin toss to make it easier to decide start player, etc.")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
