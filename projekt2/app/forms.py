# search_app/forms.py
from django import forms
from .models import YourModel

class SearchForm(forms.Form):
    sentence = forms.CharField(label='', max_length=100,required=True,initial='')

class YourModelForm(forms.ModelForm):
    class Meta:
        model = YourModel
        fields = ['name', 'email', 'message']