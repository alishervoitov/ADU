from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStamped, Authored


class User(AbstractUser, TimeStamped, Authored):
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    online = models.BooleanField(default=False)

    def get_full_name(self):
        full_name = "%s %s" % (self.last_name, self.first_name)
        return full_name.strip()

    class Meta(AbstractUser.Meta):
        verbose_name = _("Foydalanuvchi")
        verbose_name_plural = _("Foydalanuvchilar")

    def __str__(self):
        return self.username

