# Generated by Django 5.1 on 2024-09-10 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0002_course_first_sending'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='first_sending',
            new_name='updated_at',
        ),
    ]