# Generated by Django 3.0.7 on 2021-05-18 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practice_test', '0015_auto_20210518_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='categorys',
        ),
        migrations.AddField(
            model_name='quiz',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to='practice_test.QuizCategory'),
        ),
    ]
