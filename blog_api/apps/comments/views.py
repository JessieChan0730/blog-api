# Create your views here.
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Comments
from .pagination import AdminCommentPagination
from .serializer import AdminCommentSerializer


class AdminCommentViewSet(ListModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Comments.objects.all().filter(parent_comment=None)
    serializer_class = AdminCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = AdminCommentPagination

    @action(methods=['POST'], detail=False)
    def publish(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class FrontCommentViewSet():
    pass
