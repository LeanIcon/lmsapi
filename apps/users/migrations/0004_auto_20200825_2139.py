# Generated by Django 3.0.7 on 2020-08-25 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200825_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='facebook_address',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(null=True, upload_to='profile-images'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='linkedIn_address',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='location',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='timezone',
            field=models.CharField(max_length=50, null=True),
        ),
    ]