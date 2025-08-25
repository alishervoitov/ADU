from django.urls import path

from . import (
    HomePageTextListView,
    HomePageTextFilterListAPIView,
    UniversityBaseInfoView,
    FacultyListView,
    FacultyRetrieveView,
    DepartmentDetailView,
    EmployeeListView,
    DivisionDetailView,
    DivisionListByTypeView,
    MenuItemByTypeView
)

app_name = "structure"

urlpatterns = [
    path("HomePage", HomePageTextListView.as_view(), name="home_page_texts"),
    # path("HomePage", HomePageTextFilterListAPIView.as_view(), name="home_page_texts_filter"),
    path("UniversityBaseInfo", UniversityBaseInfoView.as_view(), name="university_base_info"),
    path("FacultyList", FacultyListView.as_view(), name="faculty_list"),
    path("Faculty/<int:pk>", FacultyRetrieveView.as_view(), name="faculty_detail"),
    path("Department/<int:pk>", DepartmentDetailView.as_view(), name="department_detail"),
    path("Employee", EmployeeListView.as_view(), name="employee_list"),
    path("DivisionsList/<str:division_type>", DivisionListByTypeView.as_view(), name="division_by_type"),
    path("DivisionDetail/<int:pk>", DivisionDetailView.as_view(), name="division_detail"),
    path("MenuItem/<str:menu_type>", MenuItemByTypeView.as_view(), name="menu_item_by_type"),
]
