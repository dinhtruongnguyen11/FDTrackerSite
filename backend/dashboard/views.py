from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from dashboard.serializers import *
from dashboard.models import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class FilterViewSet(viewsets.ModelViewSet):
    queryset = Filter.objects.all().order_by('-date_create')
    serializer_class = FilterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all().order_by('-date_create')
    serializer_class = KeywordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all().order_by('-date_create')
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
