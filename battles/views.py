from django.shortcuts import render, get_object_or_404
from .models import Battle
from .forms import BattleForm


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


def battle_view(request, battle_id):
    battle = get_object_or_404(Battle, pk=battle_id)

    return render(request, 'battles/battle_view.html', {'battle': battle})


def battle_edit(request, battle_id):
    battle = get_object_or_404(Battle, pk=battle_id)

    if (request.method == 'POST'):
        form = BattleForm(request.POST, instance=battle)

        if form.is_valid():
            battle = form.save(commit=False)
            battle.save()
            form.save_m2m()

            return render(request, 'battles/battle_view.html', {'battle': battle})
    else:
        form = BattleForm(instance=battle)

    return render(request, 'battles/battle_edit.html', {'form': form})
