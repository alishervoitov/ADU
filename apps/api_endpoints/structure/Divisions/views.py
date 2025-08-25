from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from apps.structure.models import Divisions, MenuItem
from apps.structure.enum import DivisionTypeEnum
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
            Divisions LIST.
            ---
            Division turlari:
            center_department - Markaz/Bo'lim
            technical_lyceum - Texnikum/Litsey
            bachelor - Bakalavriyat
            master - Magistratura
        """,
        manual_parameters=[
            openapi.Parameter(
                'division_type', openapi.IN_QUERY, description="Divisition type", type=openapi.TYPE_STRING,
                enum=[choice[0] for choice in DivisionTypeEnum.choices()]
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
    # view count ni oshirish
    def get_object(self):
        obj = super().get_object()
        obj.view_count += 1
        obj.save(update_fields=['view_count'])
        return obj


class DivisionListByTypeView(APIView):
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(
        operation_summary="Institut turi bo'yicha olish",
        operation_description="""
            Berilgan institut turi bo'yicha institut ma'lumotlarini olish.
            ---
            Institut turlari:
            center_department - Markaz/Bo'lim
            technical_lyceum - Texnikum/Litsey
            bachelor - Bakalavriyat
            master - Magistratura
            aspiranture - Aspirantura
            doctoranture - Doktorantura
        """,
        responses={
            200: serializers.DivisionListSerializer(),
            404: "Institut topilmadi"
        },
        manual_parameters=[
            openapi.Parameter(
                'division_type', openapi.IN_PATH, description="Institut turi", type=openapi.TYPE_STRING,
                enum=[choice[0] for choice in DivisionTypeEnum.choices()]
            ),
        ],
    )
    def get(self, request, division_type):
        division = Divisions.objects.filter(division_type=division_type)
        if division:
            serializer = serializers.DivisionListSerializer(division, many=True)
            return Response(serializer.data)
        else:
            return Response(
                {"detail": "Institut topilmadi"}, 
                status=status.HTTP_404_NOT_FOUND
            )
