# Generated by Django 3.0.7 on 2021-05-18 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practice_test', '0013_auto_20210518_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to='practice_test.QuizCategory'),
        ),
    ]
