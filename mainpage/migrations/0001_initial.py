# Generated by Django 5.0.6 on 2024-05-30 07:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("platform", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("instructor", models.CharField(blank=True, max_length=255, null=True)),
                ("rating", models.FloatField(blank=True, null=True)),
                ("duration", models.CharField(blank=True, max_length=50, null=True)),
                ("level", models.CharField(blank=True, max_length=50, null=True)),
                ("link", models.URLField(blank=True, max_length=500, null=True)),
                ("skills", models.TextField(blank=True, null=True)),
                ("students", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserGoal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("short_term_goal", models.CharField(max_length=255)),
                ("long_term_goal", models.CharField(max_length=255)),
                ("platform_preferences", models.CharField(max_length=255)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
