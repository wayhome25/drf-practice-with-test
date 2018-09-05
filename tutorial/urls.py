from rest_framework import routers

from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^snippets/', include('snippets.urls')),
]
