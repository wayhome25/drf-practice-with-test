from rest_framework import viewsets

from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.shortcuts import render

from quickstart.serializers import GroupSerializer
from quickstart.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
