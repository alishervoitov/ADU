from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStamped, Authored


class FAQ(TimeStamped, Authored):
    question = models.CharField(verbose_name=_("Savol"), max_length=255)
    answer = models.TextField(verbose_name=_("Javob"))
    is_active = models.BooleanField(verbose_name=_("Faol"), default=True)
    order = models.PositiveIntegerField(verbose_name=_("Tartib raqami"), default=1)

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQ lar")
        db_table = "blog_faq"

    def __str__(self):
        return self.question