# apps/DataMatrix/apps.py

from django.apps import AppConfig

class UAR(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.UAR' # Change this line USER ACCESS REQUESTS

def ready(self):
    import apps.UAR.signals