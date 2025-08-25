from rest_framework import serializers
from apps.structure.models import Divisions, Department, Employee
from apps.api_endpoints.structure.Faculty.serializers import EmployeeSerializer
from django.db.models import Q


class DivisionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divisions
        fields = ['id', 'name', 'icon']


class DivisionDetailSerializer(serializers.ModelSerializer):
    decan = EmployeeSerializer(read_only=True)
    class Meta:
        model = Divisions
        fields = ['id', 'name', 'division_type', 'content', 'banner', 'icon', 'decan']
