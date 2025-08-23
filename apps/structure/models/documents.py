from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStamped, Authored
from apps.structure.models.employees import Employee
from django_ckeditor_5.fields import CKEditor5Field


# richtext

class (TimeStamped, Authored):