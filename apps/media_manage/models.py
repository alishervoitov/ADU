from django.db import models
from apps.common.models import Authored, TimeStamped
from django_ckeditor_5.fields import CKEditor5Field


class NewType(TimeStamped, Authored):
    name = models.CharField(max_length=100, verbose_name="Type Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    class Meta:
        verbose_name = "Yangilik Turi"
        verbose_name_plural = "Yangilik Turlari"

    def __str__(self):
        return self.name


class News(TimeStamped, Authored):
    title = models.CharField(max_length=255, verbose_name="News Title")
    content = CKEditor5Field('Content', config_name='default')
    type = models.ForeignKey(
        NewType, on_delete=models.SET_NULL, related_name='news', verbose_name="Type",
        null=True, blank=True
    )
    viewed_count = models.PositiveIntegerField(default=0, verbose_name="Viewed Count")

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"

    def __str__(self):
        return self.title