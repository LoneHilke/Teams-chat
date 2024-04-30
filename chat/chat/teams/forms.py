from django import forms
from django.forms import ModelForm
from .models import Links

class LinksForm(forms.ModelForm):
  name = forms.CharField(
    widget= forms.TextInput(
    attrs={'placeholder': 'Tilføj nyt link...'}))

  class Meta:
      model = Links
      fields = '__all__'