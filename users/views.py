from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from mainpage.models import Course
from mainpage.forms import GoalForm
from mainpage.views import get_recommendations  # Import the get_recommendations function
from django.contrib.auth.forms import UserCreationForm
import random



def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.cleaned_data['goal']
            platforms = form.cleaned_data['platforms']
            recommendations = get_recommendations(goal, platforms)
            return render(request, 'users/user.html', {'recommendations': recommendations})
    else:
        form = GoalForm()
    return render(request, 'users/user.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('users:user_page')
        else:
            return render(request, "users/login.html", {"message": "Invalid Credentials"})
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('users:user_page')
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})

def user_page(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    
    enrolled_courses = request.user.enrolled_courses.all()
    recommendations = []
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.cleaned_data['goal']
            platforms = form.cleaned_data['platforms']
            recommendations = get_recommendations(goal, platforms)
    else:
        form = GoalForm()

    motivational_messages = [
            "It looks like you haven't enrolled in any courses yet. Start your learning journey now and unlock new skills!",
            "No courses enrolled yet. Let's find the perfect course for you! Get personalized recommendations now!",
            "The journey of a thousand miles begins with a single step. Take your first step by finding a course that excites you!",
            "Ready to learn something new? Get recommendations and find courses that match your goals!"
        ]
    random_message = random.choice(motivational_messages) if not enrolled_courses else None

    return render(request, 'users/user.html', {
        'form': form,
        'enrolled_courses': enrolled_courses,
        'recommendations': recommendations,
        'random_message': random_message
    })