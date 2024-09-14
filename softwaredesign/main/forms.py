# myapp/forms.py
from django import forms

class SignupForm(forms.Form):
    email = forms.EmailField(
        max_length=256,
        widget=forms.TextInput(attrs={'class':'hero-form-input w-input', 'placeholder': 'Enter your email'}),label=''
    )
    password = forms.CharField(
        max_length=256,
        widget=forms.PasswordInput(attrs={'class':'hero-form-input w-input', 'placeholder': 'Enter your password'}),label=''
    )
