from django.conf.urls import url

from snippets import views

urlpatterns = [
    url(r'^$', views.snippet_list, name='snippet_list'),
    url(r'^(?P<pk>\d+)/$', views.snippet_detail, name='snippet_detail'),
]
