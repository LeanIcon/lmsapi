# Generated by Django 3.0.7 on 2021-01-19 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practice_test', '0005_quiztaker_avg_quiz_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersanswer',
            name='answer',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='practice_test.Answer'),
            preserve_default=False,
        ),
    ]
