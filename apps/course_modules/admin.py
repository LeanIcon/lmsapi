from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Course_Module


class Modules_Admin(admin.ModelAdmin):
    list_display = ('title', 'module_number', 'course')
    search_fields = ('title', 'module_number', 'course')


admin.site.register(Course_Module, Modules_Admin)
