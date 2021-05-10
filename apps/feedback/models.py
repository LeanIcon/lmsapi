from django.db import models

# Create your models here.
from apps.courses.models import Course
from django.core.validators import MaxValueValidator, MinValueValidator


class Feedback(models.Model):
    rating = models.PositiveSmallIntegerField(default=0 ,validators=[MinValueValidator(0), MaxValueValidator(5)])
    message = models.TextField()

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='feedback')

    def __str__(self):
        return self.message

    class Meta:
        unique_together = ['message', 'rating']
        