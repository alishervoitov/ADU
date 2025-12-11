from django.db import models
from apps.common.models import Authored, TimeStamped
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class NewType(TimeStamped, Authored):
    name = models.CharField(max_length=100, verbose_name="Yangilik Turi Nomi")
    slug = models.SlugField(max_length=255, verbose_name="Slug", null=True, blank=True, unique=True)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, related_name='subtypes', verbose_name="Asosiy Turi",
        null=True, blank=True
    )
    description = models.TextField(blank=True, null=True, verbose_name="Tavsif")
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)[:50]
            slug = base_slug
            counter = 1
            while NewType.objects.filter(slug=slug).exists():
                slug = f"{base_slug[:47]}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Yangilik Turi"
        verbose_name_plural = "Yangilik Turlari"

    def __str__(self):
        return f"{self.name} ({self.parent.name})" if self.parent else self.name


class News(TimeStamped, Authored):
    title = models.CharField(max_length=255, verbose_name="Yangilik Sarlavhasi")
    slug = models.SlugField(max_length=255, verbose_name="Slug", null=True, blank=True, unique=True)
    image = models.ImageField(upload_to='news/images/', verbose_name="Asosiy rasm")
    video_url = models.URLField(max_length=255, verbose_name="Video URL", null=True, blank=True)
    content = RichTextField(verbose_name="Yangilik Matni")
    type = models.ForeignKey(
        NewType, on_delete=models.SET_NULL, related_name='news', verbose_name="Yangilik Turi",
        null=True, blank=True
    )
    created_at = models.DateTimeField(verbose_name="Yaratilgan vaqti", null=True, blank=True)
    viewed_count = models.PositiveIntegerField(default=0, verbose_name="Ko'rishlar soni")
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)[:50]
            slug = base_slug
            counter = 1
            while News.objects.filter(slug=slug).exists():
                slug = f"{base_slug[:47]}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"

    def __str__(self):
        return self.title


class DocumentType(TimeStamped, Authored):
    name = models.CharField(max_length=100, verbose_name="Hujjat turi nomi")
    slug = models.SlugField(max_length=255, verbose_name="Slug", null=True, blank=True, unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)[:50]
            slug = base_slug
            counter = 1
            while DocumentType.objects.filter(slug=slug).exists():
                slug = f"{base_slug[:47]}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Dokument Turi"
        verbose_name_plural = "Dokument Turlari"

    def __str__(self):
        return self.name


class Documents(TimeStamped, Authored):
    title = models.CharField(max_length=255, verbose_name="Hujjat nomi")
    slug = models.SlugField(max_length=255, verbose_name="Slug", null=True, blank=True, unique=True)
    url = models.URLField(max_length=255, verbose_name="URL", null=True, blank=True)
    file = models.FileField(upload_to='documents/files/', verbose_name="Hujjat fayli", null=True, blank=True)
    type = models.ForeignKey(
        DocumentType, on_delete=models.SET_NULL, related_name='documents', verbose_name="Hujjat Turi",
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