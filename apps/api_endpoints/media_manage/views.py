from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.media_manage.models import News, NewType
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class NewTypeListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        newstype = NewType.objects.all()
        serializer = serializers.NewTypeSerializer(newstype, many=True)
        return Response(serializer.data)


class NewsListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'type__name']
    filterset_fields = ['type']

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'type',
                openapi.IN_QUERY,
                description='Filter by type of News. Available types: main, global, academic, history',
                type=openapi.TYPE_STRING,
                enum=['short',],
                required=False
            )
        ],
        responses={200: serializers.NewsSerializer(many=True)},
        operation_summary="List News with filtering",
        operation_description="Get a list of News objects with optional filtering by type"
    )
    def get(self, request, *args, **kwargs):
        is_short = request.query_params.get('short', None)
        if is_short:
            self.serializer_class = serializers.NewsShortSerializer
        return super().get(request, *args, **kwargs)