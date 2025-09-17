from rest_framework import serializers
from apps.structure.models import Faculty, Employee, Department
from apps.structure.enum import WeekDaysEnum
from django.db.models import Q


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'id',
            'name',
            'code',
            'slug',
            'description',
        )

class EmployeeSerializer(serializers.ModelSerializer):
    admission_dates = serializers.SerializerMethodField()
    
    class Meta:
        model = Employee
        fields = (
            'id', 'full_name', 'employeeType', 
            'staffPosition', 'academicRank', 'academicDegree',
            'specialty', 'photo', 'email', 'phone', 'admission_dates', 
            'admission_time', 'employeeRank'
        )



class FacultyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = (
            'id',
            'name',
            'code',
            'slug',
            'description',
            'banner',
            'icon',
            
        )

class FacultyDetailSerializer(serializers.ModelSerializer):
    decan = serializers.SerializerMethodField()
    employees = serializers.SerializerMethodField()
    departments = serializers.SerializerMethodField()
    
    def get_decan(self, obj):
        return EmployeeSerializer(obj.employees.filter(staffPosition=Employee.DEKAN).first().employee).data

    def get_employees(self, obj):
        return [EmployeeSerializer(emp.employee).data for emp in obj.employees.filter(~Q(staffPosition=Employee.DEKAN))]

    def get_departments(self, obj):
        return DepartmentSerializer(obj.departments.all(), many=True).data

    class Meta:
        model = Faculty
        fields = (
            'id',
            'name',
            'code',
            'slug',
            'description',
            'banner',
            'icon',
            'position',
            'decan',
            'employees',
            'departments',
        )
