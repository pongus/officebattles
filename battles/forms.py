from django import forms
from .models import Battle, Result


class BattleForm(forms.ModelForm):
    class Meta:
        model = Battle
        fields = ['game', 'players']


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['player', 'score']
