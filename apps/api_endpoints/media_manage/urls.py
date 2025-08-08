
from django.urls import path, include
from .views import NewsListView, NewTypeListView


app_name = "media_manage"

urlpatterns = [
    path("news/", NewsListView.as_view(), name="news-list"),
    path("newstype/", NewTypeListView.as_view(), name="newstype-list"),
]