from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Teacher)
class TeacherAmin(admin.ModelAdmin):
    list_display = ['first_name',
                    'second_name']