from rest_framework.mixins import ListModelMixin, DestroyModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from .models import FriendLink
from .pagination import FriendLinkPagination
from .serializer import FriendLinkSerializer


# Create your views here.
class FriendLinksViewSet(ListModelMixin, UpdateModelMixin,DestroyModelMixin, CreateModelMixin, GenericViewSet):
    queryset = FriendLink.objects.all()
    serializer_class = FriendLinkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = FriendLinkPagination
