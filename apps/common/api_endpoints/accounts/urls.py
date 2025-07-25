from django.urls import path

from . import CustomTokenBlacklistView, CustomTokenObtainPairView, CustomTokenRefreshView


app_name = "users-api"

urlpatterns = [
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"),
    path("token/revoke/", CustomTokenBlacklistView.as_view(), name="token_revoke")
]