
from django.urls import path

from . import InteractiveServiceListView

app_name = "blog"

urlpatterns = [
    path("interactive-services/", InteractiveServiceListView.as_view(), name="interactive_service_list"),
]
