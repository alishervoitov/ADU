from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.media_manage.models import News, NewType, DocumentType, Documents
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class NewTypeListView(APIView):
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['parent']

    def get(self, request, *args, **kwargs):
        parent = request.query_params.get('parent', None)
        if parent is not None:
            newstype = NewType.objects.filter(parent__id=parent).order_by('id')
            serializer = serializers.NewTypeChildrenSerializer(newstype, many=True)
            return Response(serializer.data)
        newstype = NewType.objects.filter(parent__isnull=True).order_by('id')
        serializer = serializers.NewTypeSerializer(newstype, many=True)
        return Response(serializer.data)


class NewsListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = News.objects.all()
    serializer_class = serializers.NewsShortSerializer
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
                required=False
            )
        ],
        responses={200: serializers.NewsShortSerializer(many=True)},
        operation_summary="List News with filtering",
        operation_description="Get a list of News objects with optional filtering by type"
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class RelatedNewsListView(ListAPIView):
    permission_classes = [AllowAny]
    pagination_class = None
    serializer_class = serializers.NewsShortSerializer

    def get_queryset(self):
        type_id = self.request.query_params.get('type', None)
        if type_id is not None:
            qs = News.objects.filter(type__id=type_id).order_by('-id')
            return qs[:4]
        qs = News.objects.all().order_by('-id')
        return qs[:4]
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'type',
                openapi.IN_QUERY,
                description='Filter by type of News. Available types is numbers of NewType IDs',
                type=openapi.TYPE_STRING,
                required=False
            )
        ],
        responses={200: serializers.NewsShortSerializer(many=True)},
        operation_summary="List 4 Related News",
        operation_description="Get a list of 4 Related News objects ordered by creation date"
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class NewsListLatestView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = News.objects.all().order_by('-id')[:6]
    pagination_class = None
    serializer_class = serializers.NewsShortSerializer

    @swagger_auto_schema(
        responses={200: serializers.NewsShortSerializer(many=True)},
        operation_summary="List latest 6 News",
        operation_description="Get a list of the latest 6 News objects ordered by creation date"
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class NewsRetrieveView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk, *args, **kwargs):
        try:
            news = News.objects.get(pk=pk)
            serializer = serializers.NewsSerializer(news)
            news.viewed_count += 1
            news.save()
            return Response(serializer.data)
        except News.DoesNotExist:
            return Response({"detail": "News not found"}, status=404)


class DocumentTypeListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        document_types = DocumentType.objects.all()
        serializer = serializers.DocumentTypeSerializer(document_types, many=True)
        return Response(serializer.data)


class DocumentsListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Documents.objects.all()
    serializer_class = serializers.DocumentsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'type__name']
    filterset_fields = ['type']

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'type',
                openapi.IN_QUERY,
                description='Filter by type of Document. Available types: main, global, academic, history',
                type=openapi.TYPE_STRING,
                required=False
            )
        ],
        responses={200: serializers.DocumentsSerializer(many=True)},
        operation_summary="List Documents with filtering",
        operation_description="Get a list of Documents objects with optional filtering by type"
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class DocumentsRetrieveView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, slug, *args, **kwargs):
        try:
            document = Documents.objects.get(slug=slug)
            serializer = serializers.DocumentsSerializer(document)
            return Response(serializer.data)
        except Documents.DoesNotExist:
            return Response({"detail": "Document not found"}, status=404)