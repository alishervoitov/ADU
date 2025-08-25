from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.structure.models import Divisions
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class DivisionListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Divisions.objects.all()
    serializer_class = serializers.DivisionListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['division_type']
    pagination_class = None
    @swagger_auto_schema(
        operation_summary="Institutlar ro'yxati",
        operation_description="""
            Institutlar ro'yxati.
            ---
            Institut turlari:
            1 - Markaz/Bo'lim
            2 - Texnikum/Litsey
        """,
        manual_parameters=[
            openapi.Parameter(
                'division_type', openapi.IN_QUERY, description="Institut turi", type=openapi.TYPE_INTEGER,
                enum=[1, 2]
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class DivisionDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Divisions.objects.all()
    serializer_class = serializers.DivisionDetailSerializer
    @swagger_auto_schema(
        operation_summary="Institut tafsilotlari",
        operation_description="Berilgan ID bo'yicha institut tafsilotlarini olish",
        responses={200: serializers.DivisionDetailSerializer()},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)