# Generated by Django 3.0.7 on 2021-02-15 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_test', '0007_auto_20210119_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image_url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
