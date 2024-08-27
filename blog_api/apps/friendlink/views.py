from django_filters.rest_framework.backends import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, DestroyModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .filter import FriendLinkFilter
from .models import FriendLink
from .pagination import FriendLinkPagination
from .serializer import FriendLinkSerializer, DeleteMultiple


# Create your views here.
class FriendLinksViewSet(ListModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin, GenericViewSet):
    queryset = FriendLink.objects.all()
    # serializer_class = FriendLinkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = FriendLinkPagination
    filter_backends = (DjangoFilterBackend,)
    # 自定义过滤器
    filterset_class = FriendLinkFilter

    def get_serializer_class(self):
        if self.action == "multiple":
            return DeleteMultiple
        return FriendLinkSerializer

    @swagger_auto_schema(
        request_body=DeleteMultiple(),
        responses={}
    )
    # TODO 定义一个公共的 viewSet
    @action(methods=['delete'], detail=False)
    def multiple(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ids = serializer.data.get('ids', [])
        self.queryset.filter(id__in=ids).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
