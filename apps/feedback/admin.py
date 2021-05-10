from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Feedback


class Modules_Admin(admin.ModelAdmin):
    list_display = ('course', 'message', 'rating')
    search_fields = ('course', 'message', 'rating')


admin.site.register(Feedback, Modules_Admin)
