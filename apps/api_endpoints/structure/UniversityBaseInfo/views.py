from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from apps.structure.models import UniversityBaseInfo, Employee
from . import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class UniversityBaseInfoView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        texts = UniversityBaseInfo.objects.first()
        serializer = serializers.UniversityBaseInfoSerializer(texts)
        return Response(serializer.data)


class EmployeeListView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'staffPosition',
                openapi.IN_QUERY,
                description="Filter employees by staff position (e.g., 'rector', 'vice-rector', etc.)",
                type=openapi.TYPE_STRING,
                required=True
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        staffPosition = request.query_params.get('staffPosition', None) or None
        if not staffPosition:
            return Response({"error": "staffPosition parameter is required"}, status=400)
        employees = Employee.objects.filter(staffPosition=staffPosition)
        serializer = serializers.EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
