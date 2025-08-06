from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.structure.models import HomePageText
from . import serializers
from .filters import HomePageTextFilter
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class HomePageTextListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        texts = HomePageText.objects.all()
        serializer = serializers.HomePageSerializer(texts)
        return Response(serializer.data)



class HomePageTextFilterListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = HomePageText.objects.all()
    filterset_class = HomePageTextFilter
    serializer_class = serializers.HomePageTextSerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = None

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'type',
                openapi.IN_QUERY,
                description='Filter by type of HomePageText. Available types: main, global, academic, history',
                type=openapi.TYPE_STRING,
                enum=['main', 'global', 'academic', 'history'],
                required=False
            )
        ],
        responses={200: serializers.HomePageTextSerializer(many=True)},
        operation_summary="List HomePageText with filtering",
        operation_description="Get a list of HomePageText objects with optional filtering by type"
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)