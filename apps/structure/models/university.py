from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStamped, Authored
from apps.structure.models.employees import Employee

# class UniversityInfo(TimeStamped, Authored):
#     name = models.CharField(max_length=255, verbose_name=_("University Name"))
#     location = models.CharField(max_length=255, verbose_name=_("Location"))
#     established = models.DateField(verbose_name=_("Established Date"))

#     class Meta:
#         verbose_name = _("University Information")
#         verbose_name_plural = _("Universities Information")

#     def __str__(self):
#         return self.name
    

class Faculty(TimeStamped, Authored):
    '''Fakultet'''
    COLOR_PALETTE = [
            ("#FFFFFF", "white", ),
            ("#000000", "black", ),
            ("#0000FF", "blue",),
            ("#00FF00", "green",),
            ("#FF0000", "red",),
    ]

    name = models.CharField(max_length=255)
    xmn_id = models.CharField(max_length=20)
    code = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    banner = models.ImageField(upload_to="faculty/banner", blank=True, null=True)
    icon = models.ImageField(upload_to="faculty/icon", blank=True, null=True)
    # color = ColorField(samples=COLOR_PALETTE)
    position = models.PositiveSmallIntegerField(default=0)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'faculty'
        verbose_name = _("Faculty")
        verbose_name_plural = _("Faculties")

    
class Department(TimeStamped, Authored):
    '''Kafedra'''
    name = models.CharField(max_length=255)
    xmn_id = models.CharField(max_length=10)
    code = models.CharField(max_length=20)
    faculty = models.ForeignKey(Faculty, on_delete=models.RESTRICT, related_name="departments")
    description = models.TextField(blank=True, null=True)
    position = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'department'
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")


class Specialty(TimeStamped, Authored):
    '''Yunalish'''
    EDUCATION_TYPE = (
        (11, "Bakalavr"),
        (12, "Magistr"),
        (13, "Boshqa"),
        (14, "Doktorantura PhD"),
    )
    LOCALITY_TYPE = (
        (10, 'Boshqa'),
        (11, "Mahalliy"),
        (12, "Qo‘shma"),
        (13, "Bo'lim"),
    )
    name = models.CharField(max_length=255)
    xmn_id = models.CharField(max_length=10)
    code = models.CharField(max_length=15)
    faculty = models.ForeignKey(Faculty, on_delete=models.RESTRICT, related_name="specialities")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name="specialities", null=True)
    educationType = models.IntegerField(choices=EDUCATION_TYPE, default=11)
    localityType = models.IntegerField(choices=LOCALITY_TYPE, default=11)
    description = models.TextField(blank=True, null=True)
    position = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'specialty'
        verbose_name = _("Specialty")
        verbose_name_plural = _("Specialties")


class FacultyEmployee(TimeStamped, Authored):
    '''Fakultet xodimlari'''
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="employees")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="faculty_employees")
    position = models.CharField(max_length=255, choices=Employee.POSITION_SELECT, default=Employee.OTHER)

    class Meta:
        db_table = 'faculty_employee'
        verbose_name = _("Faculty Employee")
        verbose_name_plural = _("Faculty Employees")

    def __str__(self):
        return f"{self.id}"


class DepartmentEmployee(TimeStamped, Authored):
    '''Kafedra xodimlari'''
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="employees")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="department_employees")
    position = models.CharField(max_length=255, choices=Employee.POSITION_SELECT, default=Employee.OTHER)

    class Meta:
        db_table = 'department_employee'
        verbose_name = _("Department Employee")
        verbose_name_plural = _("Department Employees")

    def __str__(self):
        return f"{self.id}"