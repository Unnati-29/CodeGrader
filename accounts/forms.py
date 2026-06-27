from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input input-bordered w-full bg-slate-700",
                "placeholder": "Enter password",
            }
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input input-bordered w-full bg-slate-700",
                "placeholder": "Enter username",
            }
        )
    )

    class Meta:
        model = User
        fields = ["username", "password"]