from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStamped, Authored


class InteractiveService(TimeStamped, Authored):
     name = models.CharField(verbose_name=_("Xizmat nomi"), max_length=150)
     icon = models.FileField(
         verbose_name=_("Xizmat ikonkasi (light)"),
           upload_to="services/icons/",
               blank=True,
               null=True
     )
     icon_dark = models.FileField(
           verbose_name=_("Xizmat ikonkasi (dark)"),
           upload_to="services/icons/",
           blank=True,
           null=True
     )
     description = models.TextField(verbose_name=_("Xizmat haqida"), blank=True, null=True)
     link = models.CharField(
         verbose_name=_("Xizmatga havola"),
           max_length=255,
               blank=True,
               null=True
     )
     is_active = models.BooleanField(verbose_name=_("Faol"), default=True)
     order = models.PositiveIntegerField(verbose_name=_("Tartib raqami"), default=0)
     
     class Meta:
           verbose_name = _("Interaktiv xizmat")
           verbose_name_plural = _("Interaktiv xizmatlar")
           db_table = "blog_interactive_service"
     
     def __str__(self):
           return self.name           
     
     