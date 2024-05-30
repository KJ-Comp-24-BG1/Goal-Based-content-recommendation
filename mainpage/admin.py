from django.contrib import admin

# Register your models here.

from .models import Course, UserGoal

admin.site.register(UserGoal)
admin.site.register(Course)