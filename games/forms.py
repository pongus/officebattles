from django import forms


GAME_MODES = (
    (0, '1V1'),
    (1, '2V2'),
    (2, '3V3'),
    (3, '4V4'),
    (4, '5V5'),
    (5, 'FFA'),
)


class AddGameForm(forms.Form):
    name = forms.CharField(label='Game name', max_length=128)
    mode = forms.ChoiceField(choices=GAME_MODES)
    coin_toss = forms.BooleanField(label='Enable coin toss')
