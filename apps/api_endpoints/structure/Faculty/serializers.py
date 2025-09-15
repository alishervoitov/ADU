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
            'employeeRank',
            'description',
        )

class EmployeeSerializer(serializers.ModelSerializer):
    admission_dates = serializers.SerializerMethodField()
    admission_days_display = serializers.SerializerMethodField()
    
    class Meta:
        model = Employee
        fields = (
            'id', 'full_name', 'employeeType', 
            'staffPosition', 'academicRank', 'academicDegree',
            'specialty', 'photo', 'email', 'phone', 'admission_dates', 
            'admission_days_display', 'admission_time', 'employeeRank'
        )
    
    def get_admission_dates(self, obj):
        """Qabul kunlarini list sifatida qaytaradi"""
        return obj.get_admission_days_list()
    
    def get_admission_days_display(self, obj):
        """Qabul kunlarini o'zbek tilida qaytaradi"""
        days = obj.get_admission_days_display()
        # Translation obyektlarini string ga o'girish
        return [str(day) for day in days]


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
