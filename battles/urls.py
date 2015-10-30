from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^battle/new/$', views.battle_new, name='battle_new'),
    url(r'^battle/(?P<battle_id>[0-9]+)/$', views.battle_view, name='battle_view'),
    url(r'^battle/(?P<battle_id>[0-9]+)/edit/$', views.battle_edit, name='battle_edit'),
]
