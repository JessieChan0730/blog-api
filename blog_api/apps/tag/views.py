from rest_framework import viewsets

from tag.models import Tag
from tag.serializer import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
