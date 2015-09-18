from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^company/', include('companies.urls', namespace="company")),
    url(r'^admin/', include(admin.site.urls)),
]
