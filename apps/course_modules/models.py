from django.db import models

# Create your models here.

from apps.utils.models import Timestamps
from apps.courses.models import Course


class Course_Module( models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    module_number = models.IntegerField(unique=True, null=False)

    module_overview = models.TextField()

    content_one = models.TextField(null=True, blank=True)
    content_two = models.TextField(null=True, blank=True)

    duration = models.IntegerField(help_text='Enter number of hours', null=True, blank=True)

    video_url = models.CharField(max_length=255, null=True, blank=True)

    resource_url = models.CharField(max_length=255, null=True, blank=True)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['course', 'title']
        ordering = ['module_number']
