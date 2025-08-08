from rest_framework import serializers
from apps.structure.models import Faculty, Employee, Department
from apps.api_endpoints.structure.Faculty.serializers import EmployeeSerializer
from django.db.models import Q




class DepartmentDetailSerializer(serializers.ModelSerializer):
    decan = serializers.SerializerMethodField()
    employees = serializers.SerializerMethodField()

    def get_decan(self, obj):
        return EmployeeSerializer(obj.employees.filter(position=Employee.DEPARTMENT_USER).first().employee).data if obj.employees.filter(position=Employee.DEPARTMENT_USER).exists() else None

    def get_employees(self, obj):
        return [EmployeeSerializer(emp.employee).data for emp in obj.employees.filter(~Q(position=Employee.DEPARTMENT_USER))] if obj.employees.exists() else []

    class Meta:
        model = Department
        fields = (
            'id',
            'name',
            'code',
            'description',
            'decan',
            'employees',
        )

