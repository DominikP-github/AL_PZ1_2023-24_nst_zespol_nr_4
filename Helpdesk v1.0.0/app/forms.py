# MojaAplikacja/forms.py
from django import forms

class ZdanieForm(forms.Form):
    zdanie = forms.CharField(label='Wpisz zdanie', widget=forms.Textarea)
