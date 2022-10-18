from django import forms
from .models import Devotional
from django.forms.models import ModelForm

# class AddForm(ModelForm):
#     class Meta:
#         model =  Devotional
#         fields = ('image', 'title', 'date', 'scripture', 'body', 'prayer', 'day', 'month', 'year', 'further_study')
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['title'].widget.attrs.update({'class': 'form-control mb-4'})
