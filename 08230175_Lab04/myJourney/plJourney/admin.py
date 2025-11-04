from django.contrib import admin
from .models import LearningJourney, AboutMe  # Import your models from the current app

# Register your models with the Django admin site so we can manage them via the admin interface
admin.site.register(LearningJourney)  # Register the LearningJourney model
admin.site.register(AboutMe)          # Register the AboutMe model
