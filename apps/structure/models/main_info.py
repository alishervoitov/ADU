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
    
    class Meta:
        verbose_name = _("Home Page Text")
        verbose_name_plural = _("Home Page Texts")

    def __str__(self):
        return f"{self.type}: {self.title}"
    