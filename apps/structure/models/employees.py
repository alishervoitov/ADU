from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStamped, Authored
from apps.structure.enum import WeekDaysEnum
from datetime import date

from ckeditor.fields import RichTextField

class UserInfo(TimeStamped, Authored):
    '''Foydalanuvchi Umumiy Abstrakt malumotlari'''
    NONE = 'none'
    UZBEK = 'uzbek'
    OTHER = 'other'

    CITIZENSHIP = (
        (NONE, _('None')),
        ('russian', _('Russian')),
        ('kazakh', _('Kazakh')),
        ('karakalpak', _('Karakalpak')),
        ('tajik', _('Tajik')),
        ('turkmen', _('Turkmen')),
        ('kyrgyz', _('Kyrgyz')),
        ('ukrainian', _('Ukrainian')),
        ('belarusian', _('Belarusian')),
        ('armenian', _('Armenian')),
        ('korean', _('Korean')),
        ('afghan', _('Afghan')),
        (UZBEK, _("O'zbek")),
        (OTHER, _('Boshqa'))
    )

    MALE = 'male'
    FEMALE = 'female'

    GENDER_CHOISES = (
        (MALE, _('Erkak')),
        (FEMALE, _('Ayol'))
    )

    full_name = models.CharField(_("To'liq ism"), max_length=255)
    photo = models.ImageField(_("Foydalanuvchi rasmi"), upload_to="users/", null=True, blank=True)
    image = models.URLField(_("Rasm URL manzili"), null=True, blank=True)
    gender = models.CharField(_("Jinsi"), max_length=10, choices=GENDER_CHOISES)
    year_of_enter = models.CharField(_("Kirish yili"), max_length=4, null=True, blank=True)
    birthday = models.DateField(_("Tug'ilgan sana"), null=True, blank=True)
    email = models.EmailField(_("Elektron pochta"), null=True, blank=True)
    phone = models.CharField(_("Telefon raqami"), max_length=20, null=True, blank=True)
    age = models.IntegerField(_("Yosh"), default=18)

    @property
    def ages(self):
        if not self.birthday:
            return None
        today = date.today()
        return today.year - self.birthday.year - (
            (today.month, today.day) < (self.birthday.month, self.birthday.day)
        )

    def calculate_age(self):
        if not self.birthday:
            return None
        today = date.today()
        self.age = today.year - self.birthday.year - (
            (today.month, today.day) < (self.birthday.month, self.birthday.day)
        )
        self.save()

    def __str__(self):
        return self.full_name

    class Meta:
        abstract = True


class Employee(UserInfo):
    '''O'qituvchi va qolgan ishchilar malumotlari'''

    UNTITLED = "10"
    DOTSENT = "11"
    SENIOR_LECTURER = "12"
    PROFESSOR = "13"

    ACADEMIC_TITLE = (
        (UNTITLED, _("Untitled")),
        (DOTSENT, _("Dotsent")),
        (SENIOR_LECTURER, _("Senior Lecturer")),
        (PROFESSOR, _("Professor")),
    )

    FULL = "11"
    EXTERNAL = "13"
    HOURLY = "14"
    INTERNAL_ADJUNCT = "12"
    INTERNAL_MAIN = "15"

    WORK_TYPE_SELECT = (
        (FULL, _("Asosiy ish joy")),
        (EXTERNAL, _("O'rindoshlik (tashqi)")),
        (HOURLY, _("Soatbay")),
        (INTERNAL_ADJUNCT, _("O'rindoshlik (ichki-qo'shimcha)")),
        (INTERNAL_MAIN, _("O'rindoshlik (ichki-asosiy)")),
    )

    UNDEGREE = "10"
    CANDIDATE_OF_SCIENCES = "11"
    DOCTOR_OF_SCIENCES = "12"

    ACADEMIC_DEGREE = (
        (UNDEGREE, _("Darajasiz")),
        (CANDIDATE_OF_SCIENCES, _("Fan nomzodi (PhD)")),
        (DOCTOR_OF_SCIENCES, _("Fan doktori (DSc)")),
    )

    STAJYOR = "11"
    ASISTENT = "12"
    BIG_TEACHER = "13"
    DOTSENT = "14"
    PROFESSOR = "15"
    DEPARTMENT_USER = "16"
    TUTOR = "tutor"
    ENGINEER = "engineer"
    DEKAN = "dekan" 
    DEKAN_ASSISTANT = "dekan_assistant"
    OTHER = "other"

    POSITION_SELECT = (
        (STAJYOR, _("Stajor O'qituvchi")),
        (ASISTENT, _("Asistent")),
        (BIG_TEACHER, _("Katta o'qituvchi")),
        (DOTSENT, _("Dotsent")),
        (PROFESSOR, _("Professor")),
        (DEPARTMENT_USER, _('Kafedra mudiri')),
        (DEKAN, _("Dekan")),
        (DEKAN_ASSISTANT, _("Dekan muovini")),
        (TUTOR, _("Tyutor")),
        (ENGINEER, _("1-toifali muhandis")),
        (OTHER, _("Boshqa")),
        ("rector", _("Rektor")),
        ("vice-rector", _("Prorektor")),
    )

    EMPLOYEE_TYPE = (
        ("other", _("Boshqa")),
        ("teacher", _("Professor-o‘qituvchi xodim")),
        ("dekan", _("Administrativ-boshqaruv xodim")),
        ("tutor", _("O‘quv-yordamchi va texnik xodim"))
    )

    employee_id_number = models.CharField(_("Xodim ID raqami"), max_length=20, null=True, blank=True, unique=True)
    specialty = models.CharField(_("Mutaxassisligi"), max_length=255, null=True, blank=True)
    academicDegree = models.CharField(
        _("Ilmiy darajasi"), max_length=255, choices=ACADEMIC_DEGREE, default=UNDEGREE, null=True, blank=True)
    academicRank = models.CharField(
        _("Ilmiy unvoni"), max_length=255, choices=ACADEMIC_TITLE, default=UNTITLED, null=True, blank=True)
    employmentForm = models.CharField(
        _("Ish shakli"), max_length=255, choices=WORK_TYPE_SELECT, default=FULL, null=True, blank=True)
    staffPosition = models.CharField(_("Lavozimi"), max_length=255, choices=POSITION_SELECT, null=True, blank=True)
    employeeType = models.CharField(
        _("Xodim turi"), max_length=255, choices=EMPLOYEE_TYPE, default="teacher")
    is_foreign = models.BooleanField(_("Chet el fuqarosi"), default=False)
    employeeRank = models.CharField(_("Xodim darajasi"), max_length=255, null=True, blank=True)
    admission_dates = models.CharField(
        _("Qabul kunlari"), 
        max_length=255, 
        blank=True,
        help_text=_("Qabul kunlarini vergul bilan ajrating. Masalan: monday,tuesday,friday")
    )
    admission_time = models.CharField(
        _("Qabul qilingan vaqt"), max_length=50, null=True, blank=True, help_text=_("Masalan: 09:00 - 11:00")
    )
    task = RichTextField(verbose_name=_("Vazifalari"), null=True, blank=True)    
    
    def __str__(self):
        return f"{self.full_name} - {self.staffPosition}"

    @property
    def all_teachers(self):
        return self.objects.get_teachers()

    class Meta:
        db_table = 'employee'
        verbose_name = _("Xodim")
        verbose_name_plural = _("Xodimlar")
