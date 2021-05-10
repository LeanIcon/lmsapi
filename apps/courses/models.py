from django.db import models

# Create your models here.

from apps.utils.models import Timestamps


class Course( models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    course_overview = models.TextField()

    course_content_one = models.TextField(null=True)
    course_content_two = models.TextField(null=True, blank=True) 

    date = models.DateField()
    duration = models.IntegerField(help_text='Enter number of hours', null=True)


    video_url = models.CharField(max_length=255, null=True, blank=True)
    resource_url = models.CharField(max_length=255, null=True, blank=True)

    pricing = models.IntegerField(default=0, null=True, blank=True)
    category = models.CharField(max_length=255, default='uncategorized', null=True, blank=True)
    sub_category = models.CharField(
        max_length=255, default='uncategorized', null=True, blank=True)
    is_required = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.title
