from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Lesson


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson_number', 'date', 'course_module')
    search_fields = ('title', 'lesson_number', 'course')


admin.site.register(Lesson, LessonAdmin)
