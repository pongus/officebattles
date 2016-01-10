from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^battle/new/$', views.battle_new, name='battle_new'),
    url(r'^battle/(?P<battle_id>[0-9]+)/$', views.battle_view, name='battle_view'),
    url(r'^battle/(?P<battle_id>[0-9]+)/edit/$', views.battle_edit, name='battle_edit'),
    url(r'^battle/(?P<battle_id>[0-9]+)/result/new/$', views.result_new, name='result_new'),
    url(r'^battle/(?P<battle_id>[0-9]+)/result/save/$', views.result_save, name='result_save'),
    url(r'^battle/(?P<battle_id>[0-9]+)/result/view/$', views.result_view, name='result_view'),
    url(r'^battle/(?P<battle_id>[0-9]+)/result/(?P<result_id>[0-9]+)/edit/$', views.result_edit, name='result_edit'),
]
