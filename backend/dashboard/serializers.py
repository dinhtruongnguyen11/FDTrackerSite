from django.contrib.auth.models import User, Group
from rest_framework import serializers

from dashboard.models import Filter, Keyword, Alert


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class FilterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Filter
        fields = '__all__'


class KeywordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'


class AlertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'
