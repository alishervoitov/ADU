from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStamped, Authored
from apps.structure.enum import MenuItemEnum
from apps.structure.models.employees import Employee
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class MenuItem(TimeStamped, Authored):
    title = models.CharField(max_length=255, verbose_name=_("Sarlavha"))
    content = RichTextField(verbose_name=_("Kontent"))
    menu_type = models.CharField(max_length=50, choices=MenuItemEnum.choices(), verbose_name=_("Menyu turi"), unique=True)
    slug = models.SlugField(max_length=255, verbose_name=_("Slug"), null=True, blank=True, unique=True)
    position = models.PositiveSmallIntegerField(default=0, verbose_name=_("Pozitsiya"))
    view_count = models.PositiveIntegerField(default=0, verbose_name=_("Ko'rishlar soni"))

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'menu_item'
        verbose_name = _("Menyu elementi")
        verbose_name_plural = _("Menyu elementlari")
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)[:50]
            slug = base_slug
            counter = 1
            while MenuItem.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    @classmethod
    def get_by_menu_type(cls, menu_type):
        """Get MenuItem by menu_type"""
        return cls.objects.filter(menu_type=menu_type).first()
    
    def get_absolute_url(self):
        """Get the URL for this menu item"""
        return f"/api/structure/MenuItem/{self.menu_type}"


class Document(TimeStamped, Authored):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="documents", verbose_name=_("Menyu elementi"))
    name = models.CharField(max_length=150, verbose_name=_("Hujjat nomi"))
    url = models.URLField(max_length=255, verbose_name=_("URL"), null=True, blank=True)
    file = models.FileField(upload_to='documents/files/', verbose_name=_("Fayl"), null=True, blank=True)
  
    slug = models.SlugField(max_length=255, verbose_name=_("Slug"), null=True, blank=True, unique=True)

    class Meta:
        db_table = 'document_type'
        verbose_name = _("Hujjat turi")
        verbose_name_plural = _("Hujjat turlari")

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)[:50]
            slug = base_slug
            counter = 1
            while Document.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    @property 
    def get_file_or_url(self):
        if self.file:
            return self.file.url
        return self.url
