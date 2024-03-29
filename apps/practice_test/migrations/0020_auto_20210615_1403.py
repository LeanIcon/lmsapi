# Generated by Django 3.0.7 on 2021-06-15 14:03

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practice_test', '0019_auto_20210524_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizcategory',
            name='description',
            field=models.TextField(blank=True, default='N/A'),
        ),
        migrations.AlterField(
            model_name='question',
            name='label',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to='practice_test.QuizCategory'),
        ),
    ]
