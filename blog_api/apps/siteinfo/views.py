from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import SiteInfo
from .serializer import SiteInfoSerializer


# Create your views here.
class SiteInfoView(GenericViewSet):
    queryset = SiteInfo.objects.all()
    serializer_class = SiteInfoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(methods=['get'], detail=False)
    def view(self, request):
        info = self.queryset.first()
        if not info:
            info = SiteInfo.objects.create(title='关于本站', content='暂无内容')
        serializer = self.get_serializer(instance=info)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=False)
    def change(self, request):
        global serializer
        info = self.queryset.first()
        data = request.data
        if not info:
            serializer = self.get_serializer(data=data)
        else:
            serializer = self.get_serializer(instance=info, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class FrontSiteInfoView(GenericViewSet):
    queryset = SiteInfo.objects.all()
    serializer_class = SiteInfoSerializer
    permission_classes = [AllowAny]

    @action(methods=['get'], detail=False)
    def view(self, request):
        info = self.queryset.first()
        if not info:
            raise NotFound("网站信息不存在")
        serializer = self.get_serializer(instance=info)
        return Response(serializer.data, status=status.HTTP_200_OK)
