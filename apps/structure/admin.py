from django.contrib import admin
from .models.employees import Employee
from .models.university import Faculty, Department, Specialty, FacultyEmployee, DepartmentEmployee, Divisions, DivisionDocument
from .models.main_info import HomePageText, UniversityBaseInfo
from .models.documents import Document, MenuItem

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
                  'employmentForm', 'staffPosition', 'employeeType', 'is_foreign',
                  'admission_dates', 'admission_time'
                  )
            }),
            ('Tizim ma\'lumotlari', {
                  'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
                  'classes': ('collapse',)
            }),
            (
                  'Qo\'shimcha ma\'lumotlar', {
                        'fields': ('tasks',),
                        'classes': ('collapse',)
                  }
            )
      )
      
      def get_queryset(self, request):
            qs = super().get_queryset(request)
            return qs.select_related('created_by', 'updated_by')
      

class FacultyEmployeeInline(admin.TabularInline):
      model = FacultyEmployee
      extra = 1
      readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
      fields = ('employee', 'staffPosition', 'created_at', 'updated_at')
      autocomplete_fields = ('employee',)
      show_change_link = True


class DepartmentEmployeeInline(admin.TabularInline):
      model = DepartmentEmployee
      extra = 1
      readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
      fields = ('employee', 'position', 'created_at', 'updated_at')
      autocomplete_fields = ('employee',)
      show_change_link = True


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
      list_display = (
            'id', 'name', 'xmn_id', 'code', 'position', 
            'departments_count', 'specialties_count',
            'created_at', 'updated_at'
      )
      list_display_links = ('id', 'name')
      search_fields = ('name', 'xmn_id', 'code', 'description')
      prepopulated_fields = {'code': ('name',), 'slug': ('name',)}
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
            'id', 'name', 'faculty', 'xmn_id', 'code', 
            'position', 'specialties_count', 'created_at', 'updated_at'
      )
      list_display_links = ('id', 'name')
      list_filter = ('faculty', 'created_at', 'updated_at')
      search_fields = ('name', 'xmn_id', 'code', 'description', 'faculty__name')
      autocomplete_fields = ('faculty',)
      prepopulated_fields = {'code': ('name',), 'slug': ('name',)}
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
      search_fields = ('name', 'xmn_id', 'code', 'description', 'faculty__name', 'department__name')
      readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
      autocomplete_fields = ('faculty', 'department')
      ordering = ('faculty', 'department', 'position', 'name')
      prepopulated_fields = {'slug': ('name',)}
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
      
class DivisionDocumentInline(admin.TabularInline):
      model = DivisionDocument
      extra = 1
      readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
      fields = ('name', 'url', 'file', 'slug', 'created_at', 'updated_at', 'created_by', 'updated_by')
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


class DocumentInline(admin.TabularInline):
      model = Document
      extra = 1
      readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
      fields = ('name', 'url', 'file', 'slug', 'created_at', 'updated_at', 'created_by', 'updated_by')
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