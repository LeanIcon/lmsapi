# Generated by Django 3.0.7 on 2020-10-06 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_lesson_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='status',
        ),
    ]