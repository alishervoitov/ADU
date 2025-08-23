import uuid
from django.db import migrations, models

def gen_slug(apps, schema_editor):
    Department = apps.get_model('structure', 'Department')
    Faculty = apps.get_model('structure', 'Faculty')
    Specialty = apps.get_model('structure', 'Specialty')
    for obj in Department.objects.all():
        obj.slug = str(uuid.uuid4())
        obj.save(update_fields=["slug"])
    for obj in Faculty.objects.all():
        obj.slug = str(uuid.uuid4())
        obj.save(update_fields=["slug"])
    for obj in Specialty.objects.all():
        obj.slug = str(uuid.uuid4())
        obj.save(update_fields=["slug"])

class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0011_homepagetext_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Slug', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Slug', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='specialty',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Slug', blank=True, null=True),
        ),
        migrations.RunPython(gen_slug, reverse_code=migrations.RunPython.noop),
    ]