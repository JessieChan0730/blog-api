from django.urls import path

from . import views

app_name = "user"
urlpatterns = [
    path("index", views.Article.as_view())

]
