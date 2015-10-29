from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^battle/new/$', views.battle_create, name='battle_create'),
    # url(r'^battle/(?P<battle_id>[0-9])/edit/$', views.battle_edit, name='battle_edit'),
]
