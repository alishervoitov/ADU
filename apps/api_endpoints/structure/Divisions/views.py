from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from apps.structure.models import Divisions
from apps.structure.enum import DivisionTypeEnum
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class DivisionDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Divisions.objects.all()
    serializer_class = serializers.DivisionDetailSerializer
    @swagger_auto_schema(
        operation_summary="Division Detail",
        operation_description="Berilgan ID bo'yicha Division Detailni olish",
        responses={200: serializers.DivisionDetailSerializer()},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_object(self):
        obj = super().get_object()
        obj.view_count += 1
        obj.save(update_fields=['view_count'])
        return obj


class DivisionListByTypeView(APIView):
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(
        operation_summary="Division turi bo'yicha olish",
        operation_description="""
            Berilgan Division turi bo'yicha Division ma'lumotlarini olish.
            ---
            Division turlari:
            center_department - Markaz/Bo'lim
            technical_lyceum - Texnikum/Litsey
            bachelor - Bakalavriyat
            master - Magistratura
            aspiranture - Aspirantura
            doctoranture - Doktorantura
        """,
        responses={
            200: serializers.DivisionListSerializer(),
            404: "Division topilmadi"
        },
        manual_parameters=[
            openapi.Parameter(
                'division_type', openapi.IN_PATH, description="Division turi", type=openapi.TYPE_STRING,
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
                {"detail": "Division topilmadi"}, 
                status=status.HTTP_404_NOT_FOUND
            )
