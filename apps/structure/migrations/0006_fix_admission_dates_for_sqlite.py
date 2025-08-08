# Generated manually to fix SQLite compatibility

from django.db import migrations, models
from django.contrib.postgres import fields as postgres_fields


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0005_rename_position_facultyemployee_staffposition_and_more'),
    ]

    operations = [
        # migrations.RunPython(
        #     alter_admission_dates_postgresql,
        #     reverse_code=migrations.RunPython.noop,
        # ),
        # migrations.RunPython(
        #     alter_admission_dates_sqlite,
        #     reverse_code=migrations.RunPython.noop,
        # ),
    ]
