from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'course_overview', 'date')
    search_fields = ('title', 'course_overview')


admin.site.register(Course, CourseAdmin)
