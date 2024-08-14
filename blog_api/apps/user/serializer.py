from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from blog_api.utils.result.format import render_data


class ChangePasswordSerializer(serializers.Serializer):
    #  修改密码
    password = serializers.CharField(write_only=True, max_length=18)
    #  确认密码
    password2 = serializers.CharField(write_only=True, max_length=18)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("两次密码输入不一致")
        return attrs


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


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        old_data = super().validate(attrs)
        old_data['tokenType'] = 'Bearer'
        old_data['expires'] = settings.SIMPLE_JWT.get('TOKEN_EXPIRES', 30 * 60)
        new_data = render_data(code=200, data=old_data)
        return new_data
