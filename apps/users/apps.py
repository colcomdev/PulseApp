from django.apps import AppConfig
# apps/users/apps.py
from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'  # Add the 'apps.' prefix here


"""class UsersConfig(AppConfig):
    name = 'users'"""
