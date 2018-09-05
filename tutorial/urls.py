from rest_framework import routers

from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

from quickstart import views

urlpatterns = [
    url(r'^', include('snippets.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
]
