from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.utils import timezone

from offices.models import Office
from games.models import Game
from battles.models import Battle

from battles.forms import AddBattleForm

# Create your views here.
def add(request, company_id, office_id, game_id):
    office = get_object_or_404(Office, pk=office_id)
    game = get_object_or_404(Game, pk=game_id)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        add_battle_form = AddBattleForm(request.POST)
        # check whether it's valid:
        if add_battle_form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        add_battle_form = AddBattleForm()

    context = {
        'office': office,
        'game': game,
        'form': add_battle_form,
    }

    return render(request, 'battles/add.html', context)

def save(request, company_id, office_id, game_id):
    battle_game = request.POST.get('game')
    # battle_players = request.POST.get('players')
    battle_updated = timezone.now()
    battle = Battle(
        game_id = battle_game,
        # players = 1,
        updated = battle_updated
    )
    battle.save()

    return HttpResponseRedirect('/company/' + str(company_id) + '/office/' + str(office_id) + '/game/' + str(game_id) + '/battle/add')
