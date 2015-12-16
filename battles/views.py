from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Battle, Result
from .forms import BattleForm, ResultForm


def battle_new(request):
    if request.method == 'POST':
        battle_form = BattleForm(request.POST)

        if battle_form.is_valid():
            battle = battle_form.save(commit=False)
            battle.save()

            players = request.POST.getlist('players')
            for player in players:
                result = ResultForm().save(commit=False)
                result.player_id = player
                result.battle_id = battle.id
                result.save()

            context = {'battle': battle}

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
        form = ResultForm(request.POST)

        if form.is_valid():
            result = form.save(commit=False)
            result.battle_id = battle_id
            result.save()
            form.save_m2m()

            context = {'result': result}

            return render(request, 'battles/result_view.html', context)
    else:
        form = ResultForm()

    return render(request, 'battles/result_edit.html', {'form': form})


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


def result_view(request, battle_id, result_id):
    result = get_object_or_404(Result, pk=result_id)

    return render(request, 'battles/result_view.html', {'result': result})
