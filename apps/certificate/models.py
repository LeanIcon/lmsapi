from django.db import models

# Create your models here.

from apps.utils.models import Timestamps


class Certificate(Timestamps, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()