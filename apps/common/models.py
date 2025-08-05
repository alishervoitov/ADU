from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"), db_index=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"), db_index=True)
    
    @property
    def created_at_str(self):
        return self.created_at.strftime("%Y-%m-%d %H:%M:%S")
    
    @property
    def updated_at_str(self):
        return self.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        abstract = True


class Authored(models.Model):
    created_by = models.ForeignKey(
        to="users.User",
        verbose_name=_("Created by"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_created_by",
    )
    updated_by = models.ForeignKey(
        to="users.User",
        verbose_name=_("Updated by"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_updated_by",
    )

    class Meta:
        abstract = True



class FrontendTranslation(Authored, TimeStamped):
    key = models.CharField(_("Key"), max_length=255, unique=True)
    text = models.TextField(_("Text"))

    class Meta:
        db_table = "frontend_translation"
        verbose_name = _("Frontend translation")
        verbose_name_plural = _("Frontend translations")

    def __str__(self):
        return str(self.key)
