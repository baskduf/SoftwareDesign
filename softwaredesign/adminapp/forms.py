# myapp/forms.py
from django import forms

class createAIForm(forms.Form):
    ainame = forms.CharField(
        max_length=256,
        widget=forms.TextInput(attrs={'class':'hero-form-input w-input', 'placeholder': 'Enter your ainame'}),label=''
    )
    prompt = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'hero-form-input w-input', 
            'placeholder': 'Enter your prompt'
        }),
        label=''
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'onchange': 'setThumbnail(event);'}),label=''
    )
