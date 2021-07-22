from django import forms

class Login(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField()