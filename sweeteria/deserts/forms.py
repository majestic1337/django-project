from django import forms
from .models import Desert

class CandyForm(forms.ModelForm):
    class Meta:
        model = Desert
        fields = ['name', 'filling', 'price', 'img_path', 'composition', 'description']
