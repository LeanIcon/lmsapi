# Generated by Django 3.0.7 on 2021-01-14 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_test', '0003_quiztaker_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiztaker',
            name='total_quizzes_taken',
            field=models.IntegerField(default=0),
        ),
    ]
