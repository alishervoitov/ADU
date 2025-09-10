from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

from apps.api_endpoints.structure.UniversityBaseInfo.serializers import EmployeeSerializer
from apps.structure.models import Department
from . import serializers
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
                        'slug': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Slug',
                            max_length=255,
                            read_only=True
                        ),
                        'description': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Tavsif',
                            x_nullable=True
                        ),
                        'decan': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID'),
                                'full_name': openapi.Schema(type=openapi.TYPE_STRING, description='To\'liq ismi'),
                                'phone': openapi.Schema(type=openapi.TYPE_STRING, description='Telefon raqami'),
                                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email manzili'),
                                'admission_dates': openapi.Schema(type=openapi.TYPE_STRING, description='Qabul qilingan sana'),
                                'admission_time': openapi.Schema(type=openapi.TYPE_STRING, description='Qabul qilingan vaqt'),
                            },
                            description='Dekan ma\'lumotlari',
                            x_nullable=True
                        ),
                        'employees': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID'),
                                    'full_name': openapi.Schema(type=openapi.TYPE_STRING, description='To\'liq ismi'),
                                    'phone': openapi.Schema(type=openapi.TYPE_STRING, description='Telefon raqami'),
                                    'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email manzili'),
                                    'admission_dates': openapi.Schema(type=openapi.TYPE_STRING, description='Qabul qilingan sana'),
                                    'admission_time': openapi.Schema(type=openapi.TYPE_STRING, description='Qabul qilingan vaqt'),
                                }
                            ),
                            description='Xodimlar ro\'yxati',
                            read_only=True
                        ),
                    }
                )
            )
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

