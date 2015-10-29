from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Battle
from .forms import BattleForm

def battle_create(request):
    if request.method == 'POST':
        form = BattleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = BattleForm()

    return render(request, 'battles/create.html', {'form': form})
