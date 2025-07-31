from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.utils.translation import activate, get_language

from apps.common import models
from . import serializers


class FrontendTranslationView(ListCreateAPIView):
    serializer_class = serializers.FrontendTranslationSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="key",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Key",
            ),
            openapi.Parameter(
                name="lang",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Language code (uz, uz-cyrl, ru, en)",
                enum=['uz', 'uz-cyrl', 'ru', 'en']
            )
        ]
    )
    def get(self, request):
        # Tilni parametrdan olish
        lang = request.GET.get('lang', 'uz')
        
        # Tilni faollashtirish
        activate(lang)
        
        serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {}
        for obj in serializer.data:
            data[obj["key"]] = obj["text"]
        return Response(data, status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = models.FrontendTranslation.objects.all()
        key = self.request.GET.get("key", None)

        if key:
            queryset = queryset.filter(key__icontains=key)

        return queryset

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.FrontendTranslationCreateSerializer
        return serializers.FrontendTranslationSerializer


class FrontendTranslationCreateView(CreateAPIView):
    """Yangi tarjima yaratish uchun alohida view"""
    serializer_class = serializers.FrontendTranslationCreateSerializer
    permission_classes = (AllowAny,)
    
    def post(self, request):
        """Yangi tarjima yaratish"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
