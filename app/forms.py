from django import forms
from .models import Fromularz

class SearchForm(forms.Form):
    sentence = forms.CharField(label='', max_length=100,required=True,initial='')

class YourModelForm(forms.ModelForm):
    class Meta:
        model = Fromularz
        fields = ['Imie', 'email', 'Problem']

class ChangeCredentialsForm(forms.Form):
    new_email = forms.EmailField(label='Nowy Email', required=False)
    new_password1 = forms.CharField(widget=forms.PasswordInput, label='Nowe Hasło', required=False)
    new_password2 = forms.CharField(widget=forms.PasswordInput, label='Powtórz Hasło', required=False)
    old_password = forms.CharField(widget=forms.PasswordInput, label='Stare Hasło', required=False)