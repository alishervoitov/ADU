from rest_framework import serializers
from apps.structure.models import Employee, Department
# from apps.api_endpoints.structure.Faculty.serializers import EmployeeSerializer
from django.db.models import Q

class EmployeeSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()
    task = serializers.SerializerMethodField()
    
    def get_photo(self, obj):
        if obj.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.photo.url)
            return obj.photo.url
        return None
    
    def get_task(self, obj):
        if self.task:
            return self.task
        return obj.task
    
    class Meta:
        model = Employee
        fields = (
            'id', 'full_name', 'employeeType', 
            'staffPosition', 'academicRank', 'academicDegree',
            'specialty', 'photo', 'email', 'phone', 'admission_dates', 
            'admission_time', 'employeeRank', 'task'
        )


class DepartmentDetailSerializer(serializers.ModelSerializer):
    decan = serializers.SerializerMethodField()
    employees = serializers.SerializerMethodField()

    def get_decan(self, obj):
        return EmployeeSerializer(obj.employees.filter(position=Employee.DEPARTMENT_USER).first().employee, context=self.context, task=obj.employees.filter(position=Employee.DEPARTMENT_USER).first().task).data if obj.employees.filter(position=Employee.DEPARTMENT_USER).exists() else None

    def get_employees(self, obj):
        return [EmployeeSerializer(emp.employee, context=self.context, task=emp.task).data for emp in obj.employees.filter(~Q(position=Employee.DEPARTMENT_USER))] if obj.employees.exists() else []

    class Meta:
        model = Department
        fields = (
            'id',
            'name',
            'code',
            'slug',
            'description',
            'decan',
            'employees',
        )

