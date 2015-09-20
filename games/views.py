from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.utils import timezone

from companies.models import Company
from offices.models import Office
from games.models import Game

# Create your views here.
def add(request, company_id, office_id):
    company = get_object_or_404(Company, pk=company_id)
    office = get_object_or_404(Office, pk=office_id)
    context = {
        'company': company,
        'office': office,
    }
    return render(request, 'games/add.html', context)

def save(request, company_id, office_id):
    game_name = request.POST.get('game-name')
    game_updated = timezone.now()
    game = Game(company_id=company_id, office_id=office_id, name=game_name, game_mode=0, updated=game_updated)
    game.save()
    return HttpResponseRedirect('/company/' + str(company_id) + '/office/' + str(office_id) + '/game/' + str(game.id))

def list(request, company_id, office_id):
    company = get_object_or_404(Company, pk=company_id)
    office = get_object_or_404(Office, pk=office_id)
    total_game_list = Game.objects.order_by('-updated')
    company_game_list = Game.objects.filter(company_id=company_id).order_by('-updated')
    office_game_list = Game.objects.filter(office_id=office_id).order_by('-updated')
    context = {
        'company': company,
        'office': office,
        'total_game_list': total_game_list,
        'company_game_list': company_game_list,
        'office_game_list': office_game_list,
    }
    return render(request, 'games/list.html', context)

def view(request, company_id, office_id, game_id):
    company = get_object_or_404(Company, pk=company_id)
    office = get_object_or_404(Office, pk=office_id)
    game = get_object_or_404(Game, pk=game_id)
    context = {
        'company': company,
        'office': office,
        'game': game,
    }
    return render(request, 'games/view.html', context)
