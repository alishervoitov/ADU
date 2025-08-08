
from django.urls import path, include
from .views import *


app_name = "media_manage"

urlpatterns = [
    path("news/", NewsListView.as_view(), name="news-list"),
    path("news/<int:pk>/", NewsRetrieveView.as_view(), name="news-detail"),
    path("newstype/", NewTypeListView.as_view(), name="newstype-list"),
]