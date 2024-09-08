from article.models import Article
from category.models import Category

from django.db.models import Count
from django.db.models.functions.datetime import TruncDate
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from tag.models import Tag


# Create your views here.
class StatisticsAPI(APIView):
    def get(self, request: Request) -> Response:
        response_data = {}
        article_num = Article.objects.all().count()

        articles_per_day = Article.objects.annotate(
            date=TruncDate('create_date')
        ).values('date').annotate(
            sum=Count('id')
        ).order_by('date')
        articles_per_day_format = [[str(item['date']), item['sum']] for item in articles_per_day]

        latest_articles = [{'title': article.title, 'create_date': article.create_date.strftime('%Y-%m-%d')} for
                           article in
                           Article.objects.order_by('-create_date')[:6]]

        category_per_name = Category.objects.values('name').annotate(value=Count('article')).order_by('name')
        category_per_name_format = [{'name': item['name'], 'value': item['value']} for item in category_per_name]

        tags = Tag.objects.all()
        tags_format = [{"id": tag.id, "name": tag.name} for tag in tags]

        response_data['article_num'] = article_num
        response_data['articles_per_day'] = articles_per_day_format
        response_data['latest_articles'] = latest_articles
        response_data['category_per_name'] = category_per_name_format
        response_data['tags'] = tags_format
        return Response(status=status.HTTP_200_OK, data=response_data)
