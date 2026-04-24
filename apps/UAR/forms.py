from django import forms
from .models import AccessRequest
# forms.py
from .models import SecurityLog

class SecurityLogForm(forms.ModelForm):
    class Meta:
        model = SecurityLog
        fields = '__all__'

class RequestForm(forms.ModelForm):
    class Meta:
        model = AccessRequest
        fields = ['system', 'reason']