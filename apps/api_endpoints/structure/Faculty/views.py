from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from apps.structure.models import Faculty
from . import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class FacultyListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Faculty.objects.all().order_by('position')
    serializer_class = serializers.FacultyListSerializer
    pagination_class = None

class FacultyRetrieveView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Faculty.objects.all()
    serializer_class = serializers.FacultyDetailSerializer
    
    @swagger_auto_schema(
        operation_description="Faculty detallari olish",
        responses={
            200: openapi.Response(
                description="Faculty detallari",
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
                        'banner': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Banner',
                            x_nullable=True
                        ),
                        'icon': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Icon',
                            x_nullable=True
                        ),
                        'position': openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description='Position',
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
                        'departments': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID'),
                                    'name': openapi.Schema(type=openapi.TYPE_STRING, description='Kafedra nomi'),
                                    'code': openapi.Schema(type=openapi.TYPE_STRING, description='Kod'),
                                    'slug': openapi.Schema(type=openapi.TYPE_STRING, description='Slug'),
                                    'description': openapi.Schema(type=openapi.TYPE_STRING, description='Tavsif'),
                                }
                            ),
                            description='Kafedralar ro\'yxati',
                            read_only=True
                        ),
                    }
                )
            )
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
