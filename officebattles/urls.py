from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^company/', include('companies.urls', namespace="company")),
    url(r'^company/', include('offices.urls', namespace="office")),
    url(r'^company/', include('games.urls', namespace="game")),
    url(r'^company/', include('battles.urls', namespace="battle")),
    url(r'^admin/', include(admin.site.urls)),
]
