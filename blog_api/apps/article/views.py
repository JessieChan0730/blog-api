from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import  ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from article.models import Article

from article.serializers import ArticleSerializer


# Create your views here.

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [JWTAuthentication]  # 认证方式
    permission_classes = [IsAuthenticatedOrReadOnly]  # 权限类，匿名用户只读，登录用户可以操作

