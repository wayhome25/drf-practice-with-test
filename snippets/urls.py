from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import url

from snippets import views

urlpatterns = [
    url(r'^$', views.SnippetList.as_view(), name='snippet_list'),
    url(r'^(?P<pk>\d+)/$', views.SnippetDetail.as_view(), name='snippet_detail'),
    url(r'^users/$', views.UserList.as_view(), name='user_list'),
    url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view(), name='user_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
