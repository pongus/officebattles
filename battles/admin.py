from django.contrib import admin
from .models import Battle, Result


class BattleAdmin(admin.ModelAdmin):
    fields = ['game', 'completed']
    list_display = ('game', 'completed', 'created', 'updated')
    list_filter = ['game', 'completed', 'created', 'updated']
    search_fields = ['game']

admin.site.register(Battle, BattleAdmin)


class ResultAdmin(admin.ModelAdmin):
    fields = ['battle', 'player', 'score']
    list_display = ('battle', 'player', 'score', 'created', 'updated')
    list_filter = ['battle', 'player', 'created', 'updated']
    search_fields = ['battle', 'player']

admin.site.register(Result, ResultAdmin)
