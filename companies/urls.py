from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list$', views.list, name='list'),
    url(r'^add$', views.add, name='add'),
    url(r'^save$', views.save, name='save'),
    url(r'^(?P<company_id>[0-9]+)$', views.view, name='view'),
]
