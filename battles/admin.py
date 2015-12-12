from django.contrib import admin
from .models import Battle, Result


class BattleAdmin(admin.ModelAdmin):
    fields = ['game']
    list_display = ('game', 'created', 'updated')
    list_filter = ['game', 'created', 'updated']
    search_fields = ['game']

admin.site.register(Battle, BattleAdmin)


class ResultAdmin(admin.ModelAdmin):
    fields = ['battle', 'player', 'rank', 'score']
    list_display = ('battle', 'player', 'rank', 'score', 'created', 'updated')
    list_filter = ['battle', 'player', 'created', 'updated']
    search_fields = ['battle', 'player']

admin.site.register(Result, ResultAdmin)
