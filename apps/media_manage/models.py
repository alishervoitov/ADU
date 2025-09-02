from django.db import models
from apps.common.models import Authored, TimeStamped
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify


class NewType(TimeStamped, Authored):
    name = models.CharField(max_length=100, verbose_name="Type Name")
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, related_name='subtypes', verbose_name="Parent Type",
        null=True, blank=True
    )
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    class Meta:
        verbose_name = "Yangilik Turi"
        verbose_name_plural = "Yangilik Turlari"

    def __str__(self):
        return self.name


class News(TimeStamped, Authored):
    title = models.CharField(max_length=255, verbose_name="News Title")
    image = models.ImageField(upload_to='news/images/', verbose_name="Asosiy rasm")
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


class DocumentType(TimeStamped, Authored):
    name = models.CharField(max_length=100, verbose_name="Type Name")

    class Meta:
        verbose_name = "Dokument Turi"
        verbose_name_plural = "Dokument Turlari"

    def __str__(self):
        return self.name


class Documents(TimeStamped, Authored):
    title = models.CharField(max_length=255, verbose_name="Document Title")
    slug = models.SlugField(max_length=255, verbose_name="Slug", null=True, blank=True, unique=True)
    url = models.URLField(max_length=255, verbose_name="URL", null=True, blank=True)
    file = models.FileField(upload_to='documents/files/', verbose_name="File")
    type = models.ForeignKey(
        DocumentType, on_delete=models.SET_NULL, related_name='documents', verbose_name="Type",
        null=True, blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)[:50]
            slug = base_slug
            counter = 1
            while Documents.objects.filter(slug=slug).exists():
                slug = f"{base_slug[:47]}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Dokument"
        verbose_name_plural = "Dokumentlar"

    def __str__(self):
        return self.title