"""Forms of the project."""
from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description']
        widgets = {'description': forms.Textarea()}

    quantity = forms.IntegerField(
        label='quantity',
        max_value = 50,
        min_value = 0
        )
