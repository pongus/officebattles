from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^battle/new/$', views.create, name='create'),
    url(r'^battle/(?P<battle_id>[0-9])/edit/$', views.edit, name='edit'),
]
