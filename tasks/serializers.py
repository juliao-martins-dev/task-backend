from django.contrib.auth.models import User
from .models import Task
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["id"] = user.id
        token["username"] = user.username
        token["email"] = user.email

        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)

        # data["id"] = self.user.id
        # data["username"] = self.user.username
        # data["email"] = self.user.email

        user = {
            "id": self.user.id,
            "username": self.user.username,
            "email": self.user.email
        }

        data["user"] = user

        return data


class UserSerializer(serializers.HyperlinkedModelSerializer):

    tasks = serializers.HyperlinkedRelatedField(many=True, view_name='task-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'tasks']


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Task
        fields = ['url', 'id', 'title', 'completed', 'owner']