from django.contrib import admin

# Register your models here.
from .models import SecurityLog

admin.site.register(SecurityLog)
