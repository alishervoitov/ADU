from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStamped, Authored
from datetime import date


class UserInfo(TimeStamped, Authored):
    '''Foydalanuvchi Umumiy Abstrakt malumotlari'''
    NONE = 'none'
    UZBEK = 'uzbek'
    OTHER = 'other'

    CITIZENSHIP = (
        (NONE, 'None'),
        ('russian', 'Russian'),
        ('kazakh', 'Kazakh'),
        ('karakalpak', 'Karakalpak'),
        ('tajik', 'Tajik'),
        ('turkmen', 'Turkmen'),
        ('kyrgyz', 'Kyrgyz'),
        ('ukrainian', 'Ukrainian'),
        ('belarusian', 'Belarusian'),
        ('armenian', 'Armenian'),
        ('korean', 'Korean'),
        ('afghan', 'Afghan'),
        (UZBEK, 'O\'zbek'),
        (OTHER, 'Boshqa')
    )

    MALE = 'male'
    FEMALE = 'female'

    GENDER_CHOISES = (
        (MALE, 'Erkak'),
        (FEMALE, 'Ayol')
    )

    full_name = models.CharField(max_length=255)
    xmn_id = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="users/", null=True, blank=True)
    image = models.URLField(null=True,blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOISES)
    year_of_enter = models.CharField(max_length=4, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    passport = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    citizenship = models.CharField(
        max_length=255, choices=CITIZENSHIP, default=UZBEK)
    age = models.IntegerField(default=18)

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
        (UNTITLED, "Untitled"),
        (DOTSENT, "Dotsent"),
        (SENIOR_LECTURER, "Senior Lecturer"),
        (PROFESSOR, "Professor"),
    )

    FULL = "11"
    EXTERNAL = "13"
    HOURLY = "14"
    INTERNAL_ADJUNCT = "12"
    INTERNAL_MAIN = "15"

    WORK_TYPE_SELECT = (
        (FULL, "Asosiy ish joy"),
        (EXTERNAL, "O'rindoshlik (tashqi)"),
        (HOURLY, "Soatbay"),
        (INTERNAL_ADJUNCT, "O'rindoshlik (ichki-qo'shimcha)"),
        (INTERNAL_MAIN, "O'rindoshlik (ichki-asosiy)"),
    )

    UNDEGREE = "10"
    CANDIDATE_OF_SCIENCES = "11"
    DOCTOR_OF_SCIENCES = "12"

    ACADEMIC_DEGREE = (
        (UNDEGREE, "Darajasiz"),
        (CANDIDATE_OF_SCIENCES, "Fan nomzodi (PhD)"),
        (DOCTOR_OF_SCIENCES, "Fan doktori (DSc)"),
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
        # TEACHERS = "O'qituvchilar",
        (STAJYOR, "Stajor O'qituvchi"),
        (ASISTENT, "Asistent"),
        (BIG_TEACHER, "Katta o'qituvchi"),
        (DOTSENT, "Dotsent"),
        (PROFESSOR, "Professor"),
        # OTHER = "Boshqa",
        (DEPARTMENT_USER, 'Kafedra mudiri'),
        (DEKAN, "Dekan"),
        (DEKAN_ASSISTANT, "Dekan muovini"),
        (TUTOR, "Tyutor"),
        (ENGINEER, "1-toifali muhandis"),
        (OTHER, "Boshqa")
    )

    EMPLOYEE_TYPE = (
        ("other", "Boshqa"),
        ("teacher", "Professor-o‘qituvchi xodim"),
        ("dekan", "Administrativ-boshqaruv xodim"),
        ("tutor", "O‘quv-yordamchi va texnik xodim")
    )

    employee_id_number = models.CharField(max_length=20)
    meta_id = models.CharField(max_length=20)
    uzkadr_id = models.CharField(max_length=10)
    specialty = models.CharField(max_length=255, null=True, blank=True)
    academicDegree = models.CharField(
        max_length=255, choices=ACADEMIC_DEGREE, default=UNDEGREE)
    academicRank = models.CharField(
        max_length=255, choices=ACADEMIC_TITLE, default=UNTITLED)
    employmentForm = models.CharField(
        max_length=255, choices=WORK_TYPE_SELECT, default=FULL)
    staffPosition = models.CharField(max_length=255, choices=POSITION_SELECT)
    employeeType = models.CharField(
        max_length=255, choices=EMPLOYEE_TYPE, default="teacher")
    is_foreign = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} - {self.staffPosition}"

    @property
    def all_teachers(self):
        return self.objects.get_teachers()

    class Meta:
        db_table = 'employee'

