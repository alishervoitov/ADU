from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response    
from apps.blog.models import InteractiveService
from apps.media_manage.models import News
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

BASE_URLS_DATA = {
    # 'interactive_services': InteractiveService,
    'news': News
}


class SearchServiceListView(APIView):
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(
        operation_description="Global qidiruv",
        manual_parameters=[
            openapi.Parameter(
                'query',
                openapi.IN_QUERY,
                description="Qidiruv so'rovi",
                type=openapi.TYPE_STRING,
                required=True
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', '')
        if not query:
            return Response({"results": []})
        
        data = News.objects.filter(title__icontains=query)
        search_data = []

        for item in data:
            search_data.append({
                "id": item.id,
                "name": item.title,
                "link": f"/news/{item.type.slug}/{item.slug}/"
            })

        return Response({"results": search_data})
