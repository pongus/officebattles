from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^list$', views.company_list, name='company_list'),
    url(r'^new$', views.company_new, name='company_new'),
    url(r'^(?P<company_id>[0-9]+)$', views.company_view, name='company_view'),
    url(r'^(?P<company_id>[0-9]+)/edit$', views.company_edit, name='company_edit'),
    url(r'^delete/company/(?P<company_id>[0-9]+)$',views.company_delete, name='company_delete'),
    url(r'^(?P<company_id>[0-9]+)/logo-upload$', views.logo_upload, name='logo_upload'),
]
