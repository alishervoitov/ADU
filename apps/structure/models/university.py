from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStamped, Authored
from apps.structure.models.employees import Employee
from apps.structure.enum import DivisionTypeEnum
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Faculty(TimeStamped, Authored):
    '''Fakultet'''
    COLOR_PALETTE = [
        ("#FFFFFF", "white", ),
        ("#000000", "black", ),
        ("#0000FF", "blue",),
        ("#00FF00", "green",),
        ("#FF0000", "red",),
    ]

    name = models.CharField(max_length=255, verbose_name=_("Fakultet nomi"))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_("Slug"), blank=True)
    code = models.CharField(max_length=20, verbose_name=_("Kod"), null=True, blank=True)
    description = models.TextField(blank=True, null=True, verbose_name=_("Tavsif"))
    banner = models.ImageField(upload_to="faculty/banner", blank=True, null=True, verbose_name=_("Banner"))
    icon = models.ImageField(upload_to="faculty/icon", blank=True, null=True, verbose_name=_("Ikon"))
    # color = ColorField(samples=COLOR_PALETTE)
    position = models.PositiveSmallIntegerField(default=0, verbose_name=_("Joylashuv Tartibi"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'faculty'
        verbose_name = _("Fakultet")
        verbose_name_plural = _("Fakultetlar")

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)[:50]
            slug = base_slug
            counter = 1
            while Faculty.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Department(TimeStamped, Authored):
    '''Kafedra'''
    name = models.CharField(max_length=255, verbose_name=_("Kafedra nomi"))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_("Slug"), blank=True)
    code = models.CharField(max_length=20, verbose_name=_("Kod"), null=True, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.RESTRICT, related_name="departments", verbose_name=_("Fakultet"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Tavsif"))
    position = models.PositiveSmallIntegerField(default=0, verbose_name=_("Joylashuv Tartibi"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'department'
        verbose_name = _("Kafedra")
        verbose_name_plural = _("Kafedralar")

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)[:50]
            slug = base_slug
            counter = 1
            while Department.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Specialty(TimeStamped, Authored):
    '''Yunalish'''
    EDUCATION_TYPE = (
        (11, _("Bakalavr")),
        (12, _("Magistr")),
        (13, _("Boshqa")),
        (14, _("Doktorantura PhD")),
    )
    LOCALITY_TYPE = (
        (10, _('Boshqa')),
        (11, _("Mahalliy")),
        (12, _("Qo‘shma")),
        (13, _("Bo'lim")),
    )
    name = models.CharField(max_length=255, verbose_name=_("Yo'nalish nomi"))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_("Slug"), blank=True)
    code = models.CharField(max_length=15, verbose_name=_("Kod"))
    faculty = models.ForeignKey(Faculty, on_delete=models.RESTRICT, related_name="specialities", verbose_name=_("Fakultet"))
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name="specialities", null=True, verbose_name=_("Kafedra"))
    educationType = models.IntegerField(choices=EDUCATION_TYPE, default=11, verbose_name=_("Ta'lim turi"))
    localityType = models.IntegerField(choices=LOCALITY_TYPE, default=11, verbose_name=_("Mahalliylik turi"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Tavsif"))
    position = models.PositiveSmallIntegerField(default=0, verbose_name=_("Joylashuv Tartibi"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'specialty'
        verbose_name = _("Yo'nalish")
        verbose_name_plural = _("Yo'nalishlar")

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)[:50]
            slug = base_slug
            counter = 1
            while Specialty.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
        

class FacultyEmployee(TimeStamped, Authored):
    '''Fakultet xodimlari'''
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="employees", verbose_name=_("Fakultet"))
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="faculty_employees", verbose_name=_("Xodim"))
    task = RichTextField(verbose_name=_("Vazifalari"), null=True, blank=True)
    staffPosition = models.CharField(max_length=255, choices=Employee.POSITION_SELECT, default=Employee.OTHER, verbose_name=_("Lavozim"))
    order = models.PositiveSmallIntegerField(default=0, verbose_name=_("Tartib raqami"))

    class Meta:
        db_table = 'faculty_employee'
        verbose_name = _("Fakultet xodimi")
        verbose_name_plural = _("Fakultet xodimlari")

    def __str__(self):
        return f"{self.id}"


class DepartmentEmployee(TimeStamped, Authored):
    '''Kafedra xodimlari'''
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="employees", verbose_name=_("Kafedra"))
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="department_employees", verbose_name=_("Xodim"))
    task = RichTextField(verbose_name=_("Vazifalari"), null=True, blank=True)
    position = models.CharField(max_length=255, choices=Employee.POSITION_SELECT, default=Employee.OTHER, verbose_name=_("Lavozim"))

    class Meta:
        db_table = 'department_employee'
        verbose_name = _("Kafedra xodimi")
        verbose_name_plural = _("Kafedra xodimlari")

    def __str__(self):
        return f"{self.id}"


class Divisions(TimeStamped, Authored):
    '''Division'''
    name = models.CharField(max_length=255, verbose_name=_("Division nomi"))
    code = models.CharField(max_length=20, verbose_name=_("Kod"), null=True, blank=True)
    division_type = models.CharField(max_length=50, choices=DivisionTypeEnum.choices, verbose_name=_("Division turi"))
    content = RichTextField(verbose_name=_("Tavsif"), null=True, blank=True)
    banner = models.ImageField(upload_to="institution/banner", blank=True, null=True, verbose_name=_("Banner"))
    icon = models.ImageField(upload_to="institution/icon", blank=True, null=True, verbose_name=_("Ikon"))
    position = models.PositiveSmallIntegerField(default=0, verbose_name=_("Joylashuv Tartibi"))
    decan = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, related_name="institutions", verbose_name=_("Dekan"),
        null=True, blank=True
    )   
    slug = models.SlugField(max_length=255, verbose_name=_("Slug"), null=True, blank=True, unique=True)
    view_count = models.PositiveIntegerField(default=0, verbose_name=_("Ko'rishlar soni"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'institution'
        verbose_name = _("Division")
        verbose_name_plural = _("Divisions")

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)[:50]
            slug = base_slug
            counter = 1
            while Divisions.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class DivisionDocument(TimeStamped, Authored):
    division = models.ForeignKey(Divisions, on_delete=models.CASCADE, related_name="documents", verbose_name=_("Institut"))
    name = models.CharField(max_length=150, verbose_name=_("Hujjat nomi"))
    url = models.URLField(max_length=255, verbose_name=_("URL"), null=True, blank=True)
    file = models.FileField(upload_to='documents/files/', verbose_name=_("Fayl"), null=True, blank=True)
  
    slug = models.SlugField(max_length=255, verbose_name=_("Slug"), null=True, blank=True, unique=True)

    class Meta:
        db_table = 'division_document'
        verbose_name = _("Institut hujjati")
        verbose_name_plural = _("Institut hujjatlari")

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)[:50]
            slug = base_slug
            counter = 1
            while DivisionDocument.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    @property 
    def get_file_or_url(self):
        if self.file:
            return self.file.url
        return self.url
