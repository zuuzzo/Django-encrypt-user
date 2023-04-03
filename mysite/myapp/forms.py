from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)