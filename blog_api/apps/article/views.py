from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.

# def index(request):
#     return JsonResponse(data={
#         "hello": "hello world"
#     })


class Article(APIView):
    authentication_classes = [JWTAuthentication]  # 登录认证
    permission_classes = [IsAuthenticated]  # 配置了权限类，没登录的就没有权限访问了

    def get(self, request):
        return Response({'测试测试'})
