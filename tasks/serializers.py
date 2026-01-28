from django.contrib.auth.models import User
from .models import Task

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    tasks = serializers.HyperlinkedRelatedField(many=True, view_name='task-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'tasks']


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Task
        fields = ['url', 'title', 'completed', 'owner']