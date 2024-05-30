from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course
from .forms import GoalForm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import numpy as np

def index(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.cleaned_data['goal']
            platforms = form.cleaned_data['platforms']
            recommendations = get_recommendations(goal, platforms)
            return render(request, 'mainpage/recommendations.html', {'recommendations': recommendations})
    else:
        form = GoalForm()
    return render(request, 'mainpage/index.html', {'form': form})

def add_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.user.is_authenticated:
        course.users_enrolled.add(request.user)
    return redirect('users:user_page')

def get_recommendations(user_input, platforms):
    all_courses = Course.objects.filter(platform__in=platforms)
    all_courses_list = list(all_courses)
    descriptions = [course.description for course in all_courses_list if course.description]

    if not descriptions:
        return [{'title': 'No recommendations available due to empty descriptions'}]

    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(descriptions)

    prompt_vector = tfidf_vectorizer.transform([user_input])
    cosine_similarities = linear_kernel(prompt_vector, tfidf_matrix).flatten()

    course_indices = np.argsort(cosine_similarities)[::-1].astype(int)
    
    recommended_courses = [all_courses_list[i] for i in course_indices[:5]]

    recommendations = [{
        'id': course.id,
        'title': course.title,
        'platform': course.platform,
        'link': course.link,
        'description': course.description,
        'instructor': course.instructor,
        'rating': course.rating,
        'duration': course.duration,
        'level': course.level
    } for course in recommended_courses]

    return recommendations
