from django import forms
from .models import Application
from django.forms import ModelForm

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['q1', 'q2', 'q3', 'q4']