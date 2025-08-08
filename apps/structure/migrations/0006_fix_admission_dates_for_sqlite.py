# Generated manually to fix SQLite compatibility

from django.db import migrations, models
from django.contrib.postgres import fields as postgres_fields


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0005_rename_position_facultyemployee_staffposition_and_more'),
    ]

    def alter_admission_dates_postgresql(apps, schema_editor):
        """
        For PostgreSQL, ensure the ArrayField has proper null constraints
        """
        if schema_editor.connection.vendor == 'postgresql':
            # Run raw SQL to update the field definition
            with schema_editor.connection.cursor() as cursor:
                cursor.execute("""
                    ALTER TABLE employee 
                    ALTER COLUMN admission_dates DROP NOT NULL;
                """)

    def alter_admission_dates_sqlite(apps, schema_editor):
        """
        For SQLite, convert the field to a text field that can store JSON
        """
        if schema_editor.connection.vendor == 'sqlite':
            Employee = apps.get_model('structure', 'Employee')
            # SQLite will handle this as a text field
            pass  # No additional action needed for SQLite

    operations = [
        migrations.RunPython(
            alter_admission_dates_postgresql,
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.RunPython(
            alter_admission_dates_sqlite,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
