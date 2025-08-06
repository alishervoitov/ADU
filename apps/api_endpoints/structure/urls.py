
from django.urls import path

from . import (
    HomePageTextListView,
    HomePageTextFilterListAPIView,
    UniversityBaseInfoView,
)

app_name = "structure"

urlpatterns = [
    path("home", HomePageTextListView.as_view(), name="home_page_texts"),
    path("HomePage", HomePageTextFilterListAPIView.as_view(), name="home_page_texts_filter"),
    path("UniversityBaseInfo", UniversityBaseInfoView.as_view(), name="university_base_info"),
]
