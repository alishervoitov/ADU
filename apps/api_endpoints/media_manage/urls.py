
from django.urls import path, include
from .views import *


app_name = "media_manage"

urlpatterns = [
    path("news/", NewsListView.as_view(), name="news-list"),
    path("news_latest/", NewsListLatestView.as_view(), name="news-latest"),
    path("related_news/", RelatedNewsListView.as_view(), name="related-news"),
    path("news/<int:pk>/", NewsRetrieveView.as_view(), name="news-detail"),
    path("news_type", NewTypeListView.as_view(), name="news_type-list"),
    path("document_type/", DocumentTypeListView.as_view(), name="document_type-list"),
    path("documents/", DocumentsListView.as_view(), name="documents-list"),
    path("documents/<slug:slug>/", DocumentsRetrieveView.as_view(), name="documents-detail"),
]