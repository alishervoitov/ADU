from django.urls import path, include

urlpatterns = [
    path("auth/", include("apps.api_endpoints.accounts.urls", namespace="users-api")),
    path("common/", include("apps.api_endpoints.common.urls", namespace="common")),
    path("blog/", include("apps.api_endpoints.blog.urls", namespace="blog")),
    path("structure/", include("apps.api_endpoints.structure.urls", namespace="structure")),
    path("media_manage/", include("apps.api_endpoints.media_manage.urls", namespace="media_manage")),
]
