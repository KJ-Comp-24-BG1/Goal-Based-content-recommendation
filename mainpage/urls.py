from django.urls import path
from . import views

app_name = "mainpage"
urlpatterns = [
    path("", views.index, name= "index"),
    path("recommendations/", views.get_recommendations, name='recommendations'),
    path('add_course/<int:course_id>/', views.add_course, name='add_course'),

]