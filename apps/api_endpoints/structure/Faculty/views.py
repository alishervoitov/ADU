from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.structure.models import Faculty
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
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
