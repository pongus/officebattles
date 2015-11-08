from django.shortcuts import render, get_object_or_404
from .models import Battle, Result
from .forms import BattleForm, ResultForm


def battle_new(request):
    if request.method == 'POST':
        form = BattleForm(request.POST)

        if form.is_valid():
            battle = form.save(commit=False)
            battle.save()
            form.save_m2m()

            return render(request, 'battles/battle_view.html', {'battle': battle})
    else:
        form = BattleForm()

    return render(request, 'battles/battle_edit.html', {'form': form})


def battle_edit(request, battle_id):
    battle = get_object_or_404(Battle, pk=battle_id)

    if request.method == 'POST':
        form = BattleForm(request.POST, instance=battle)

        if form.is_valid():
            battle = form.save(commit=False)
            battle.save()
            form.save_m2m()

            return render(request, 'battles/battle_view.html', {'battle': battle})
    else:
        form = BattleForm(instance=battle)

    return render(request, 'battles/battle_edit.html', {'form': form})


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

            return render(request, 'battles/result_view.html', {'result': result})

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

            return render(request, 'battles/result_view.html', {'result': result})

    else:
        form = ResultForm(instance=result)

    return render(request, 'battles/result_edit.html', {'form': form})


def result_view(request, battle_id, result_id):
    result = get_object_or_404(Result, pk=result_id)

    return render(request, 'battles/result_view.html', {'result': result})
