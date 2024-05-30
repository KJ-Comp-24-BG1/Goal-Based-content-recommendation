from django.urls import path
from . import views

app_name = "users"
urlpatterns =[
    path("", views.index, name="user_page"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('user_page/', views.user_page, name='user_page'),
    path("register/", views.register_view, name="register"),

] 