from django import forms
from .models import Battle, Result


class BattleForm(forms.ModelForm):
    class Meta:
        model = Battle
        fields = ['game']


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['player', 'rank', 'score']
