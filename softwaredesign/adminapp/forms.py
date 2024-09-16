# myapp/forms.py
from django import forms

from django import forms

class createAIForm(forms.Form):
    ainame = forms.CharField(
        max_length=256,
        widget=forms.TextInput(attrs={'class':'hero-form-input w-input', 'placeholder': 'Enter your ainame'}),
        label='캐릭터 이름'
    )
    prompt = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'hero-form-input w-input', 
            'placeholder': 'Enter your prompt'
        }),
        label='프롬프트(생략시 기본 프롬프트 적용)'
    )
    personality = forms.ChoiceField(
        choices=[
            ('calm', '차분함'),
            ('active', '활발함'),
            ('tsundere', '츤데레'),
            ('playful', '장난꾸러기'),
            ('mysterious', '신비로움'),
            ('intelligent', '지적인')
        ],
        widget=forms.Select(attrs={'class': 'hero-form-input w-input'}),
        label='성격 종류'
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'onchange': 'setThumbnail(event);'}),
        label='대표 사진'
    )

