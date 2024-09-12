from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(request=self.context['request'], username=username, password=password)
        if user is None:
            raise AuthenticationFailed({
                'detail': '用户名或者密码错误',
            })
        if not user.is_active:
            raise AuthenticationFailed({
                'detail': '用户已被禁用',
            })
        return_data = super().validate(attrs)
        return_data['tokenType'] = 'Bearer'
        return_data['expires'] = settings.SIMPLE_JWT.get('TOKEN_EXPIRES', 30 * 60)
        return return_data
