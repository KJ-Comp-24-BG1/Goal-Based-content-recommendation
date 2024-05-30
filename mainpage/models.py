from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.db import models
from django import forms

# mainpage/models.py


class Course(models.Model):
    platform = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.CharField(max_length=255, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    level = models.CharField(max_length=50, blank=True, null=True)
    link = models.URLField(max_length=500, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    students = models.IntegerField(blank=True, null=True)
    users_enrolled = models.ManyToManyField(User, related_name='enrolled_courses', blank=True)

    
    def __str__(self):
        return self.title



class UserGoal(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    short_term_goal = models.CharField(max_length=255)
    long_term_goal = models.CharField(max_length=255)
    platform_preferences = models.CharField(max_length=255)
