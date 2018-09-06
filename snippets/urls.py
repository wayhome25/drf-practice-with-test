from rest_framework.routers import DefaultRouter

from django.conf.urls import include
from django.conf.urls import url

from snippets import views


router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, base_name='snippet')
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
