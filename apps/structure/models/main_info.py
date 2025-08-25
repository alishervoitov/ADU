from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStamped, Authored

MENU_PARTS = (
    ("main", "Asosiy Sahifasi"),
    ("global", "Global"),
    ("academic", "Akademic"),
    ("history", "Tarix")
)

class HomePageText(TimeStamped, Authored):
    type = models.CharField(
        max_length=20,
        choices=MENU_PARTS,
        verbose_name=_("Type")
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_("Title")
    )
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
        null=True
    )
    url = models.URLField(
        verbose_name=_("URL"),
        blank=True,
        null=True
    )
    banner = models.ImageField(
        upload_to='home_page/',
        verbose_name=_("Banner Image"),
        blank=True,
        null=True
    )
    
    class Meta:
        verbose_name = _("Home Page Text")
        verbose_name_plural = _("Home Page Texts")

    def __str__(self):
        return f"{self.type}: {self.title}"


class UniversityBaseInfo(TimeStamped, Authored):
    about = models.TextField(
        verbose_name=_("Universitet haqida"),
        blank=True,
        null=True
    )
    students_count = models.PositiveIntegerField(
        verbose_name=_("Talabalar soni"),
        blank=True,
        null=True
    )
    teachers_count = models.PositiveIntegerField(
        verbose_name=_("O'qituvchilar soni"),
        blank=True,
        null=True
    )
    faculty_count = models.PositiveIntegerField(
        verbose_name=_("Fakultetlar soni"),
        blank=True,
        null=True
    )
    department_count = models.PositiveIntegerField(
        verbose_name=_("Kafedralar soni"),
        blank=True,
        null=True
    )
    image_1 = models.ImageField(
        upload_to='university/',
        verbose_name=_("Rasm 1"),
        blank=True,
        null=True
    )
    image_2 = models.ImageField(
        upload_to='university/',
        verbose_name=_("Rasm 2"),
        blank=True,
        null=True
    )
    phone_num = models.CharField(
        max_length=20,
        verbose_name=_("Telefon raqami"),
        blank=True,
        null=True
    )
    email = models.EmailField(
        verbose_name=_("Email"),
        blank=True,
        null=True
    )
    address = models.CharField(
        max_length=255,
        verbose_name=_("Manzil"),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Universitet asosiy ma'lumotlari")
        verbose_name_plural = _("Universitet asosiy ma'lumotlari")

    def __str__(self):
        return f"{self.id}"
    