from rest_framework import viewsets

from user.models import UserDetail
from user.serializer import UserDetailSerializer


# Create your views here.
class UserDetailViewSet(viewsets.ModelViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
