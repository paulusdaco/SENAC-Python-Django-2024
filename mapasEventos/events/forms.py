from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        #fields = ['name', 'date', 'time', 'image', 'latitude', 'longitude', 'category', 'price', 'language']
        fields = ['name', 'description', 'date', 'time', 'image', 'latitude', 'longitude', 'category', 'price', 'language',
         'created_at']


