from rest_framework import serializers
from apps.structure.models import UniversityBaseInfo, Employee


class UniversityBaseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityBaseInfo
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id',
            'full_name',
            'phone',
            'email',
            'admission_dates',
            'admission_time',
            'photo',
            'task'
        )


class EmployeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id',
            'full_name',
            'phone',
            'email',
            'admission_dates',
            'admission_time',
            'staffPosition',
            'photo',
            'task'
        )