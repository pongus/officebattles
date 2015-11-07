from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<company_id>[0-9]+)/office/add$', views.add, name='add'),
    url(r'^(?P<company_id>[0-9]+)/office/save$', views.save, name='save'),
    url(r'^(?P<company_id>[0-9]+)/office/list$', views.list, name='list'),
    url(r'^(?P<company_id>[0-9]+)/office/(?P<office_id>[0-9]+)$', views.view, name='view'),
]
