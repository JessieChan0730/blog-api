from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserDetail


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class UserDetailSerializer(serializers.Serializer):
    signature = serializers.CharField(max_length=255, required=False)
    hobby = serializers.JSONField(required=False)
    avatar = serializers.URLField(required=False)
    social_contact = serializers.JSONField(required=False)
    about_me = serializers.CharField(required=False)
    user = UserSerializer(read_only=True)
