#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# This file is the entry point for Django administrative commands like:
# python manage.py runserver, migrate, createsuperuser, etc.

import os
import sys

def main():
    """Run administrative tasks."""
    # Set the default settings module for the Django project
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myJourney.settings')

    try:
        # Import Django's command-line utility
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raise a helpful error if Django is not installed or virtual environment not activated
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Execute the command-line utility with the arguments passed to manage.py
    execute_from_command_line(sys.argv)

# This ensures that the main() function runs when manage.py is executed directly
if __name__ == '__main__':
    main()
