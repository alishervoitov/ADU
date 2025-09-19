
from django.urls import path

from . import (
    InteractiveServiceListView,
    FAQListView,
    ContactCreateView,
    SearchServiceListView,
)

app_name = "blog"

urlpatterns = [
    path("interactive-services/", InteractiveServiceListView.as_view(), name="interactive_service_list"),
    path("faqs/", FAQListView.as_view(), name="faq_list"),
    path("contact", ContactCreateView.as_view(), name="contact_create"),
    path("GlobalSearch/", SearchServiceListView.as_view(), name="global_search"),
]
