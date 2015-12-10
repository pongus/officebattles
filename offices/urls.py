from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<company_id>[0-9]+)/office/new$', views.office_new, name='office_new'),
    url(r'^(?P<company_id>[0-9]+)/office/list$', views.office_list, name='office_list'),
    url(r'^(?P<company_id>[0-9]+)/office/(?P<office_id>[0-9]+)$', views.office_view, name='office_view'),
]
