from django.shortcuts import render  # Import render to return HTML templates
from .models import LearningJourney, AboutMe  # Import your models to fetch data from the database

# Index page — Learning Journey
def index(request):
    """
    View function for the main Learning Journey page.
    
    - Fetches all LearningJourney records from the database.
    - Passes them to the template 'plJourney/index.html' using context dictionary.
    """
    journeys = LearningJourney.objects.all()  # Query all LearningJourney objects
    return render(request, 'plJourney/index.html', {'journeys': journeys})  # Render template with context

# About Me page
def about_me(request):
    """
    View function for the About Me page.
    
    - Fetches the first AboutMe record from the database (assuming only one profile exists).
    - Passes it to the template 'plJourney/aboutMe.html' using context dictionary.
    """
    about = AboutMe.objects.first()  # Get the first AboutMe object
    return render(request, 'plJourney/aboutMe.html', {'about': about})  # Render template with context
