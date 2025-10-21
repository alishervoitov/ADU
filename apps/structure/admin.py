from django.contrib import admin
from .models.employees import Employee
from .models.university import Faculty, Department, Specialty, FacultyEmployee, DepartmentEmployee, Divisions, DivisionDocument
from .models.main_info import HomePageText, UniversityBaseInfo
from .models.documents import Document, MenuItem


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
      list_display = (
            'id', 'full_name',  
            'academicDegree', 'academicRank', 'employmentForm', 'is_foreign',
            'created_at', 'updated_at'
      )
      list_display_links = ('id', 'full_name')
      list_filter = (
            'gender', 'staffPosition', 'academicDegree', 'academicRank', 
            'employmentForm', 'employeeType',
            'created_at', 'updated_at'
      )
      search_fields = (
            'full_name', 
      )

      
      def get_queryset(self, request):
            qs = super().get_queryset(request)
            return qs.select_related('created_by', 'updated_by')
      

class FacultyEmployeeInline(admin.StackedInline):
      model = FacultyEmployee
      extra = 1
      readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
      # fields = ('employee', 'staffPosition', 'task', 'order')
      autocomplete_fields = ('employee',)
      show_change_link = True


class DepartmentEmployeeInline(admin.StackedInline):
      model = DepartmentEmployee
      extra = 1
      readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
      # fields = ('employee', 'position', 'task')
      autocomplete_fields = ('employee',)
      show_change_link = True


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
      list_display = (
            'id', 'name', 'code', 'position', 
            'departments_count', 'specialties_count',
            'created_at', 'updated_at'
      )
      list_display_links = ('id', 'name')
      search_fields = ('name', 'code', 'description')
      prepopulated_fields = {'slug': ('name',)}
      readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
      inlines = [FacultyEmployeeInline]
      
      @admin.display(description='Kafedralar soni')
      def departments_count(self, obj):
            return obj.departments.count()
      
      @admin.display(description='Yo\'nalishlar soni')
      def specialties_count(self, obj):
            return obj.specialities.count()


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
      list_display = (
            'id', 'name', 'faculty', 'code', 
            'position', 'specialties_count', 'created_at', 'updated_at'
      )
      list_display_links = ('id', 'name')
      list_filter = ('faculty', 'created_at', 'updated_at')
      search_fields = ('name', 'code', 'description', 'faculty__name')
      autocomplete_fields = ('faculty',)
      prepopulated_fields = {'slug': ('name',)}
      inlines = [DepartmentEmployeeInline]
      readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
      
      
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
      search_fields = ('name', 'code', 'description', 'faculty__name', 'department__name')
      readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
      autocomplete_fields = ('faculty', 'department')
      ordering = ('faculty', 'department', 'position', 'name')
      prepopulated_fields = {'slug': ('name',)}
 
      
            
@admin.register(HomePageText)
class HomePageTextAdmin(admin.ModelAdmin):
      list_display = ('id', 'title', 'created_at', 'updated_at')
      list_display_links = ('id', 'title')
      search_fields = ('title', 'content')
      readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')


@admin.register(UniversityBaseInfo)
class UniversityBaseInfoAdmin(admin.ModelAdmin):
      list_display = (
             'students_count', 'teachers_count',
            'faculty_count', 'department_count', 'phone_num',
            'email', 'address', 'created_at', 'updated_at'
      )
      
class DivisionDocumentInline(admin.StackedInline):
      model = DivisionDocument
      extra = 1
      readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
      # fields = ('name', 'url', 'file', 'slug', 'created_at', 'updated_at', 'created_by', 'updated_by')
      show_change_link = True
      prepopulated_fields = {'slug': ('name',)}
      autocomplete_fields = ('division',)


@admin.register(Divisions)
class DivisionsAdmin(admin.ModelAdmin):
      list_display = (
            'id', 'name', 'division_type', 'code', 'position',
            'created_at', 'updated_at'
      )
      list_display_links = ('id', 'name')
      list_filter = ('division_type', 'created_at', 'updated_at')
      search_fields = ('name', 'code', 'content')
      readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
      prepopulated_fields = {'slug': ('name',)}
      inlines = [DivisionDocumentInline]


class DocumentInline(admin.StackedInline):
      model = Document
      extra = 1
      readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
      # fields = ('name', 'url', 'file', 'slug', 'created_at', 'updated_at', 'created_by', 'updated_by')
      show_change_link = True
      prepopulated_fields = {'slug': ('name',)}
      autocomplete_fields = ('menu_item',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
      list_display = (
            'id', 'title', 'menu_type', 'position', 'view_count',
            'created_at', 'updated_at'
      )
      list_display_links = ('id', 'title')
      list_filter = ('menu_type', 'created_at', 'updated_at')
      search_fields = ('title', 'content', 'menu_type')
      readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by', 'view_count')
      prepopulated_fields = {'slug': ('title',)}
      ordering = ('position', 'title')
      inlines = [DocumentInline]
