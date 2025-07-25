from django.urls import path, include

urlpatterns = [
    path("auth/", include("apps.common.api_endpoints.accounts.urls", namespace="users-api")),
    path("common/", include("apps.common.api_endpoints.common.urls", namespace="common")),
]
