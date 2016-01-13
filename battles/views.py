from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from battles.models import Battle, Result
from battles.forms import BattleForm, ResultForm
from games.models import Game
import random


def battle_list(request):
    battles = Battle.objects.filter(completed=True).order_by('-updated')

    context = {
        'battles': battles
        # Home Team / Player 1 name(s)
        # Away Team / Player 2 name(s)
        # Score home - away
    }

    return render(request, 'battles/battle_list.html', context)


def battle_new(request):
    if request.method == 'POST':
        battle_form = BattleForm(request.POST)

        if battle_form.is_valid():
            battle = battle_form.save(commit=False)
            battle.save()

            game = get_object_or_404(Game, pk=battle.game_id)
            player_ids = request.POST.getlist('players')
            random_id = random.choice(player_ids)

            for player_id in player_ids:
                result = ResultForm().save(commit=False)
                result.player_id = player_id
                result.battle_id = battle.id

                if game.coin_toss and player_id == random_id:
                    result.coin = True

                result.save()

            context = {
                'battle': battle,
                'results': Result.objects.filter(battle_id=battle.id)
            }

            return render(request, 'battles/result_edit.html', context)
    else:
        battle_form = BattleForm()

    context = {
        'players': User.objects.all(),
        'battle_form': battle_form
    }

    return render(request, 'battles/battle_edit.html', context)


def battle_edit(request, battle_id):
    battle = get_object_or_404(Battle, pk=battle_id)

    if request.method == 'POST':
        form = BattleForm(request.POST, instance=battle)

        if form.is_valid():
            battle = form.save(commit=False)
            battle.save()
            form.save_m2m()

            context = {'battle': battle}

            return render(request, 'battles/battle_view.html', context)
    else:
        form = BattleForm(instance=battle)

    context = {
        'players': User.objects.all(),
        'form': form
    }

    return render(request, 'battles/battle_edit.html', context)


def battle_view(request, battle_id):
    battle = get_object_or_404(Battle, pk=battle_id)

    return render(request, 'battles/battle_view.html', {'battle': battle})


def result_new(request, battle_id):
    if request.method == 'POST':
        scores = request.POST.getlist('scores')
        for score in scores:
            form = ResultForm(request.POST).save(commit=False)
            form.battle_id = 1
            form.player_id = 1
            form.score = score
            form.save()

        context = {'form': form}

        return render(request, 'battles/result_view.html', context)
    else:
        form = ResultForm()

    return render(request, 'battles/result_edit.html', {'form': form})


def result_save(request, battle_id):
    if request.method == 'POST':
        current_battle = Result.objects.filter(battle_id=battle_id)

        for player_id in request.POST:
            if player_id.isdigit():
                result = get_object_or_404(current_battle, player_id=player_id)
                result.score = request.POST[player_id]
                result.save()

        battle = get_object_or_404(Battle, pk=battle_id)
        battle.completed = True
        battle.save()

    return HttpResponseRedirect('/battle/list/')


def result_edit(request, battle_id, result_id):
    result = get_object_or_404(Result, pk=result_id)

    if request.method == 'POST':
        form = ResultForm(request.POST, instance=result)

        if form.is_valid():
            result = form.save(commit=False)
            result.battle_id = battle_id
            result.save()
            form.save_m2m()

            context = {'result': result}

            return render(request, 'battles/result_view.html', context)
    else:
        form = ResultForm(instance=result)

    return render(request, 'battles/result_edit.html', {'form': form})


def result_view(request, battle_id):
    battle = get_object_or_404(Battle, pk=battle_id)

    return render(request, 'battles/result_view.html', {'battle': battle})


# Start of a possibly new user flow below, not even close to be ready yet!


# Step 1 - Select game
def battle_select_game(request):
    if request.method == 'POST':
        battle_form = BattleForm(request.POST)

        if battle_form.is_valid():
            battle = battle_form.save(commit=False)
            battle.save()

            context = {
                'battle_id': battle.id,
                # TODO: Add filter for same company and same game
                'players': User.objects.all()
            }

            return render(request, 'battles/battle_select_players.html', context)
    else:
        battle_form = BattleForm()

    context = {
        'battle_form': battle_form
    }

    return render(request, 'battles/battle_select_game.html', context)


# Step 2 - Select players
def battle_select_players(request, battle_id):
    if request.method == 'POST':
        players = request.POST.getlist('players')
        for player in players:
            result = ResultForm().save(commit=False)
            result.battle_id = battle_id
            result.player_id = player
            result.save()

        context = {
            'results': Result.objects.filter(battle_id=battle_id)
        }

        return render(request, 'battles/battle_add_result.html', context)

    context = {
        'players': User.objects.all()
    }

    return render(request, 'battles/battle_select_players.html', context)


# Step 3 - Add result
def battle_add_result(request, battle_id):
    return True


# Step 4 - Save
def battle_save(request, battle_id):
    return True
