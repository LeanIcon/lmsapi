# Generated by Django 3.0.7 on 2020-10-07 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(blank=True, default='uncategorized', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='pricing',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='sub_category',
            field=models.CharField(blank=True, default='uncategorized', max_length=255, null=True),
        ),
    ]
