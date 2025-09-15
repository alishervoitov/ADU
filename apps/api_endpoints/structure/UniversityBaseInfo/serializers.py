from rest_framework import serializers
from apps.structure.models import UniversityBaseInfo, Employee


class UniversityBaseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityBaseInfo
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()
    
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
            'task',
            'employeeRank'
        )
    
    def get_photo(self, obj):
        if obj.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.photo.url)
            return obj.photo.url
        return None


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
            'task',
            'employeeRank'
        )