from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.utils import timezone

from offices.models import Office
from games.models import Game
from battles.models import Battle

from .forms import BattleForm

# Create your views here.
def create(request):
    # office = get_object_or_404(Office, pk=office_id)
    # game = get_object_or_404(Game, pk=1)

    if request.method == 'POST':
        form = BattleForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            # return HttpResponseRedirect('blog.views.post_detail', pk=post.pk)

    else:
        form = BattleForm()

    return render(request, 'battles/create.html', {'form': form})

def edit(request, battle_id):
    battle = get_object_or_404(Battle, pk=battle_id)

    if request.method == "POST":
        form = BattleForm(request.POST, instance=battle)

        if form.is_valid():
            battle = form.save(commit=False)
            battle.save()

            # return HttpResponseRedirect('blog.views.post_detail', pk=post.pk)

        else:
            form = BattleForm(instance=battle)

        return HttpResponseRedirect('battle/edit.html', {'form': form})



    # # if this is a POST request we need to process the form data
    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     battle_form = BattleForm(request.POST)
    #     # check whether it's valid:
    #     if battle_form.is_valid():
    #         # process the data in form.cleaned_data as required
    #         # ...
    #         # redirect to a new URL:
    #         return HttpResponseRedirect('/')

    # # if a GET (or any other method) we'll create a blank form
    # else:
    #     battle_form = BattleForm()

    # context = {
    #     'office': office,
    #     'game': game,
    #     'form': battle_form,
    # }

    # return render(request, 'battles/edit.html', context)

# def save(request, company_id, office_id, game_id):
#     battle_game = request.POST.get('game')
#     # battle_players = request.POST.get('players')
#     battle_updated = timezone.now()
#     battle = Battle(
#         game_id = battle_game,
#         # players = 1,
#         updated = battle_updated
#     )
#     battle.save()

#     return HttpResponseRedirect('/company/' + str(company_id) + '/office/' + str(office_id) + '/game/' + str(game_id) + '/battle/add')
