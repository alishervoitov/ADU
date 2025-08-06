
from django.urls import path

from . import (
    InteractiveServiceListView,
    FAQListView
)

app_name = "blog"

urlpatterns = [
    path("interactive-services/", InteractiveServiceListView.as_view(), name="interactive_service_list"),
    path("faqs/", FAQListView.as_view(), name="faq_list"),
]
