from django.contrib import admin

# Register your models here.
from .models import Battle, Result

class BattleAdmin(admin.ModelAdmin):
    fields = ['game', 'players']
    list_display = ('game', 'created', 'updated')
    list_filter = ['game', 'players', 'created', 'updated']
    search_fields = ['game', 'players']

admin.site.register(Battle, BattleAdmin)

class ResultAdmin(admin.ModelAdmin):
    fields = ['battle', 'player', 'rank', 'score']
    list_display = ('battle', 'player', 'rank', 'score', 'created', 'updated')
    list_filter = ['battle', 'player', 'created', 'updated']
    search_fields = ['battle', 'player']

admin.site.register(Result, ResultAdmin)
