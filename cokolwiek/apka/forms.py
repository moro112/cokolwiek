from django import forms
from django.core.validators import EmailValidator, URLValidator
from .models import *


class LoginForm(forms.Form):
    login = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class UserForm(forms.Form):
    first_name = forms.CharField(label='Imie')
    last_name = forms.CharField(label='Nazwisko')
    login = forms.CharField(label='login')
    password = forms.CharField(widget=forms.PasswordInput())


class MoneyForm(forms.Form):
    value = forms.IntegerField(label='kwota')

