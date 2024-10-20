from article.models import Article
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters

from .models import Comments


class ArticleTitleFilter(filters.FilterSet):
    article_pk = filters.NumberFilter(method='filter_by_article_pk')

    def filter_by_article_pk(self, queryset, name, value):
        if value:
            article = get_object_or_404(Article, pk=value)
            return queryset.filter(article_pk=article).all()
        return queryset

    class Meta:
        model = Comments
        fields = ["article_pk"]
