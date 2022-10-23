"""Forms of the project."""
from django import forms
from .models import Thing
from django.core.validators import RegexValidator

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description']
        widgets = {'description': forms.Textarea()}

    quantity = forms.IntegerField(
        label='quantity',
        widget = forms.NumberInput()
