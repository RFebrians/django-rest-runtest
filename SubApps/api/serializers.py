from rest_framework import serializers
from . import models


class BirthdaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Birthday
        fields = ('name', 'date', 'note')


class PasswordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Password
        fields = ('website', 'username', 'password')


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Todo
        fields = ('id', 'todoText', 'isCompleted')