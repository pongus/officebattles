from games.models import Game
from django.contrib.auth.models import User

from django import forms

class AddBattleForm(forms.Form):
    game = forms.ModelChoiceField(queryset=Game.objects.all())
    players = forms.ModelChoiceField(queryset=User.objects.all())
