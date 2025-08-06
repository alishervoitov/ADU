from django.contrib import admin
from django.utils.html import format_html
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from .models.employees import Employee
from .models.university import Faculty, Department, Specialty, FacultyEmployee, DepartmentEmployee
from .models.main_info import HomePageText

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
      list_display = (
            'id', 'full_name', 'employee_id_number', 'staffPosition', 
            'academicDegree', 'academicRank', 'employmentForm', 'is_foreign',
            'created_at', 'updated_at'
      )
      list_display_links = ('id', 'full_name')
      list_filter = (
            'gender', 'staffPosition', 'academicDegree', 'academicRank', 
            'employmentForm', 'employeeType', 'is_foreign', 'citizenship',
            'created_at', 'updated_at'
      )
      search_fields = (
            'full_name', 'employee_id_number', 'xmn_id', 'meta_id', 
            'uzkadr_id', 'specialty', 'email', 'phone', 'passport'
      )
      readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by', 'ages')
      
      fieldsets = (
            ('Asosiy ma\'lumotlar', {
                  'fields': (
                  'full_name', 'xmn_id', 'employee_id_number', 'meta_id', 'uzkadr_id',
                  'photo', 'image', 'gender', 'year_of_enter'
                  )
            }),
            ('Shaxsiy ma\'lumotlar', {
                  'fields': (
                  'birthday', 'age', 'email', 'phone', 'passport', 
                  'address', 'citizenship'
                  )
            }),
            ('Kasbiy ma\'lumotlar', {
                  'fields': (
                  'specialty', 'academicDegree', 'academicRank', 
                  'employmentForm', 'staffPosition', 'employeeType', 'is_foreign'
                  )
            }),
            ('Tizim ma\'lumotlari', {
                  'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
                  'classes': ('collapse',)
            })
      )
      
      def get_queryset(self, request):
            qs = super().get_queryset(request)
            return qs.select_related('created_by', 'updated_by')
      
      

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
      list_display = (
            'id', 'name', 'xmn_id', 'code', 'position', 
            'departments_count', 'specialties_count',
            'created_at', 'updated_at'
      )
      list_display_links = ('id', 'name')
      list_filter = ('created_at', 'updated_at')
      search_fields = ('name', 'xmn_id', 'code', 'description')
      readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
      prepopulated_fields = {'code': ('name',)}
      ordering = ('position', 'name')
      
      fieldsets = (
            ('Asosiy ma\'lumotlar', {
                  'fields': ('name', 'xmn_id', 'code', 'description', 'position')
            }),
            ('Media fayllar', {
                  'fields': ('banner', 'icon'),
                  'classes': ('collapse',)
            }),
            ('Tizim ma\'lumotlari', {
                  'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
                  'classes': ('collapse',)
            })
      )
      
      @admin.display(description='Kafedralar soni')
      def departments_count(self, obj):
            return obj.departments.count()
      
      @admin.display(description='Yo\'nalishlar soni')
      def specialties_count(self, obj):
            return obj.specialities.count()
      
      

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
      list_display = (
            'id', 'name', 'faculty', 'xmn_id', 'code', 
            'position', 'specialties_count', 'created_at', 'updated_at'
      )
      list_display_links = ('id', 'name')
      list_filter = ('faculty', 'created_at', 'updated_at')
      search_fields = ('name', 'xmn_id', 'code', 'description', 'faculty__name')
      readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
      autocomplete_fields = ('faculty',)
      ordering = ('faculty', 'position', 'name')
      
      fieldsets = (
            ('Asosiy ma\'lumotlar', {
                  'fields': ('name', 'xmn_id', 'code', 'faculty', 'description', 'position')
            }),
            ('Tizim ma\'lumotlari', {
                  'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
                  'classes': ('collapse',)
            })
      )
      
      @admin.display(description='Yo\'nalishlar soni')
      def specialties_count(self, obj):
            return obj.specialities.count()
      
      

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
      list_display = (
            'id', 'name', 'faculty', 'department', 'code', 
            'educationType', 'localityType', 'position',
            'created_at', 'updated_at'
      )
      list_display_links = ('id', 'name')
      list_filter = (
            'faculty', 'department', 'educationType', 'localityType',
            'created_at', 'updated_at'
      )
      search_fields = ('name', 'xmn_id', 'code', 'description', 'faculty__name', 'department__name')
      readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
      autocomplete_fields = ('faculty', 'department')
      ordering = ('faculty', 'department', 'position', 'name')
      
      fieldsets = (
            ('Asosiy ma\'lumotlar', {
                  'fields': ('name', 'xmn_id', 'code', 'faculty', 'department')
            }),
            ('Ta\'lim ma\'lumotlari', {
                  'fields': ('educationType', 'localityType', 'description', 'position')
            }),
            ('Tizim ma\'lumotlari', {
                  'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
                  'classes': ('collapse',)
            })
      )
      
      

@admin.register(FacultyEmployee)
class FacultyEmployeeAdmin(admin.ModelAdmin):
      list_display = (
            'id', 'faculty', 'employee_name', 'employee_id', 'position',
            'created_at', 'updated_at'
      )
      list_display_links = ('id',)
      list_filter = ('faculty', 'position', 'created_at', 'updated_at')
      search_fields = (
            'faculty__name', 'employee__full_name', 'employee__employee_id_number',
            'position'
      )
      readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
      autocomplete_fields = ('faculty', 'employee')
      
      fieldsets = (
            ('Asosiy ma\'lumotlar', {
                  'fields': ('faculty', 'employee', 'position')
            }),
            ('Tizim ma\'lumotlari', {
                  'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
                  'classes': ('collapse',)
            })
      )
      
      @admin.display(description='Xodim ismi')
      def employee_name(self, obj):
            return obj.employee.full_name if obj.employee else '-'
      
      @admin.display(description='Xodim ID')
      def employee_id(self, obj):
            return obj.employee.employee_id_number if obj.employee else '-'
      
      

@admin.register(DepartmentEmployee)
class DepartmentEmployeeAdmin(admin.ModelAdmin):
      list_display = (
            'id', 'department', 'department_faculty', 'employee_name', 
            'employee_id', 'position', 'created_at', 'updated_at'
      )
      list_display_links = ('id',)
      list_filter = (
            'department__faculty', 'department', 'position', 
            'created_at', 'updated_at'
      )
      search_fields = (
            'department__name', 'department__faculty__name',
            'employee__full_name', 'employee__employee_id_number', 'position'
      )
      readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
      autocomplete_fields = ('department', 'employee')
      
      fieldsets = (
            ('Asosiy ma\'lumotlar', {
                  'fields': ('department', 'employee', 'position')
            }),
            ('Tizim ma\'lumotlari', {
                  'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
                  'classes': ('collapse',)
            })
      )
      
      @admin.display(description='Fakultet')
      def department_faculty(self, obj):
            return obj.department.faculty.name if obj.department and obj.department.faculty else '-'
      
      @admin.display(description='Xodim ismi')
      def employee_name(self, obj):
            return obj.employee.full_name if obj.employee else '-'
      
      @admin.display(description='Xodim ID')
      def employee_id(self, obj):
            return obj.employee.employee_id_number if obj.employee else '-'
      

@admin.register(HomePageText)
class HomePageTextAdmin(admin.ModelAdmin):
      list_display = ('id', 'title', 'created_at', 'updated_at')
      list_display_links = ('id', 'title')
      search_fields = ('title', 'content')
      readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
      