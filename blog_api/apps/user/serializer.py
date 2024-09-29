from django.contrib.auth.models import User
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate
from rest_framework import serializers

from .const import json_schema


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
    nickname = serializers.CharField(required=False, min_length=1, max_length=15)
    signature = serializers.CharField(max_length=255, min_length=1, required=False)
    avatar = serializers.ImageField(required=False, label="图片", use_url=True, error_messages={
        'invalid': '图片参数错误'
    })
    more_info = serializers.JSONField(required=False)

    def validate_more_info(self, value):
        try:
            validate(value, json_schema)
            return value
        except ValidationError as e:
            raise serializers.ValidationError(e)

    def update(self, instance, validated_data):
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.signature = validated_data.get('signature', instance.signature)
        instance.more_info = validated_data.get('more_info', instance.more_info)
        instance.save()
        return instance

