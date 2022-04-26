from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserProfile


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'name': 'username', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'name': 'email', 'class': 'form-control', 'placeholder': 'Email kiriting'})
        }
