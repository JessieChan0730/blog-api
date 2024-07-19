from annual_summary.models import AnnualSummary
from annual_summary.serializer import AnnualSummarySerializer
from drf_yasg import openapi
from drf_yasg.openapi import Parameter
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class AnnualSummaryViewSet(GenericViewSet):
    serializer_class = AnnualSummarySerializer
    queryset = AnnualSummary.objects.all()
    authentication_classes = [JWTAuthentication]  # 认证方式
    permission_classes = [IsAuthenticatedOrReadOnly]  # 权限类，匿名用户只读，登录用户可以操作

    # 生成
    def create(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        # 保存
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    #  查看年报详情
    @swagger_auto_schema(
        responses={status.HTTP_200_OK: AnnualSummarySerializer()},
        manual_parameters=[Parameter(name='year', in_=openapi.IN_PATH, required=True, type=openapi.TYPE_NUMBER)]
    )
    def look(self, request: Request, year: int) -> Response:
        annual = AnnualSummary.objects.filter(create_year=year).first()
        if annual is None:
            return Response(data={
                "code": status.HTTP_404_NOT_FOUND,
                "message": "没有该年份的年报"
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = AnnualSummarySerializer(annual)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    # 获取列表
    def list(self, request: Request) -> Response:
        annuals = AnnualSummary.objects.all()
        if len(annuals) == 0:
            return Response(data={
                "code": status.HTTP_404_NOT_FOUND,
                "message": "还没发布一篇年度总结"
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = AnnualSummarySerializer(annuals, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    # 更新年报
    def update(self, request, year):
        annual = AnnualSummary.objects.filter(create_year=year).first()
        data = request.data
        if annual is None:
            return Response(data={
                "code": status.HTTP_404_NOT_FOUND,
                "message": "没有该年份的年报"
            })
        serializer = self.get_serializer(instance=annual, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    # http://localhost:8080/api/annual/{year} get:查看某个年份的年报
    # http://localhost:8080/api/annual  post:生成 put:更新 get:获取所有
