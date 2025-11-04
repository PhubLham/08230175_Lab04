from django.shortcuts import render

# Create your views here.
from .models import LearningJourney, AboutMe

# Index page — Learning Journey
def index(request):
    journeys = LearningJourney.objects.all()
    return render(request, 'plJourney/index.html', {'journeys': journeys})

# About Me page
def about_me(request):
    about = AboutMe.objects.first()
    return render(request, 'plJourney/aboutMe.html', {'about': about})
