
from django.urls import path

from . import (
    HomePageTextListView,
    HomePageTextFilterListAPIView,
    UniversityBaseInfoView,
    FacultyListView,
    FacultyRetrieveView,
)

app_name = "structure"

urlpatterns = [
    path("HomePage", HomePageTextListView.as_view(), name="home_page_texts"),
    # path("HomePage", HomePageTextFilterListAPIView.as_view(), name="home_page_texts_filter"),
    path("UniversityBaseInfo", UniversityBaseInfoView.as_view(), name="university_base_info"),
    path("Faculty", FacultyListView.as_view(), name="faculty_list"),
    path("Faculty/<int:pk>", FacultyRetrieveView.as_view(), name="faculty_detail"),
]
