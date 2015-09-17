from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^(?P<company_id>[0-9]+)/$', views.view, name='view'),
    url(r'^(?P<company_id>[0-9]+)/view$', views.view, name='view'),
]
