from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.models import UserDetail
from user.serializer import UserDetailSerializer, ChangePasswordSerializer


class UserDetailViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]  # 认证方式
    permission_classes = [IsAuthenticatedOrReadOnly]  # 权限类，匿名用户只读，登录用户可以操作
    queryset = UserDetail.objects.all()

    # 访问action时，使用ChangePasswordSerializer序列化器
    def get_serializer_class(self):
        # 如果用户的action是password则使用ChangePasswordSerializer序列化器
        if self.action == 'password':
            return ChangePasswordSerializer
        return UserDetailSerializer

    # 修改密码
    @action(detail=False, methods=['POST'])
    def password(self, request: Request) -> Response:
        # 获取用户需要修改的密码
        password = request.data.get('password', '')
        if request.user.is_authenticated:
            user_id = request.user.id
            try:
                user = User.objects.get(id=user_id)
                user.set_password(password)
                user.save()
                return Response(
                    data={
                        'message': '修改密码成功'
                    }, status=status.HTTP_200_OK
                )
            except User.DoesNotExist:
                return Response(data={
                    'message': '用户不存在'
                }, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(data={
                'message': '您还未通过认证'
            }, status=status.HTTP_401_UNAUTHORIZED)
