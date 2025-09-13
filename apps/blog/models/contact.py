from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStamped, Authored


class Contact(TimeStamped, Authored):
    full_name = models.CharField(verbose_name=_("F.I.Sh."), max_length=255)
    phone = models.CharField(verbose_name=_("Telefon raqami"), max_length=50)
    message = models.CharField(verbose_name=_("Xabar"), max_length=1000)

    class Meta:
        verbose_name = _("Aloqa")
        verbose_name_plural = _("Aloqa lar")
        db_table = "blog_contact"

    def __str__(self):
        return f"{self.full_name} - {self.phone}"
