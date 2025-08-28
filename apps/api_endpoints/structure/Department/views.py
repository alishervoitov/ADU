from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.api_endpoints.structure.UniversityBaseInfo.serializers import EmployeeSerializer
from apps.structure.models import Department, Employee
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class DepartmentDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentDetailSerializer
    
    @swagger_auto_schema(
        operation_description="Department detallari olish",
        responses={
            200: openapi.Response(
                description="Department detallari",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description='ID',
                            read_only=True
                        ),
                        'name': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Kafedra nomi',
                            max_length=255,
                            min_length=1
                        ),
                        'code': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Kod',
                            max_length=20,
                            x_nullable=True
                        ),
                        'description': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Tavsif',
                            x_nullable=True
                        ),
                        'decan': EmployeeSerializer,
                        'employees': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=EmployeeSerializer,
                            description='Employees',
                            read_only=True
                        ),
                    }
                )
            )
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
