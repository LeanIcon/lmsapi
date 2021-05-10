from django.db import models

# Create your models here.

from apps.utils.models import Timestamps
from apps.course_modules.models import Course_Module
from django.contrib.auth import get_user_model
from django.conf import settings

class Lesson(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    lesson_number = models.IntegerField(unique=True, null=False)
    # lecturer_name = models.CharField(max_length=100, default='',blank=True)
    content_one = models.TextField()
    content_two = models.TextField(null=True, blank=True)
    content_three = models.TextField(null=True, blank=True)
    date = models.DateField(null=True)
    duration = models.IntegerField(help_text='Enter number of hours', null=True)

    video_one = models.CharField(max_length=255, null=True)
    video_two = models.CharField(max_length=255, null=True, blank=True)

    resource_url = models.CharField(max_length=255, null=True)

    course_module = models.ForeignKey(Course_Module, on_delete=models.CASCADE, related_name='lessons')
    # status = models.ForeignKey(
    #     Lesson_Status, on_delete=models.CASCADE, related_name='status')

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['course_module', 'title']
        ordering = ['lesson_number']


class Lesson_Status(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)


# =================================== #
# Note :
# lessons order sholud not be unique
# Meta ordering should be changed to course module
# =================================== #
