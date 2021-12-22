from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from .models import ClaimsModel


class ClaimModelForm(forms.ModelForm):

    class Meta:
        CHOICES_FOR_LOSS_TYPES = (
            ("Own Damage", "Own Damage"),
            ("Knock for Knock", "Knock for Knock"),
            ("Windscreen Damage", "Windscreen Damage"),
            ("Theft", "Theft")
        )

        BINARY_CHOICES = [
            ("Yes", "Yes"),
            ("No", "No")]

        model = ClaimsModel
        fields = '__all__'
        widgets = {
            "date": forms.widgets.DateInput(attrs={'type': 'date'}),
            "time:": forms.widgets.TimeInput(attrs={'type': 'time'}),
            "typeOfLoss": forms.Select(choices=CHOICES_FOR_LOSS_TYPES),
            "description": forms.Textarea,
            "isPoliceReported": forms.Select(choices=BINARY_CHOICES),
            "isInjured": forms.Select(choices=BINARY_CHOICES),
            # Hide update status field from user
            "updateStatus": forms.HiddenInput(),
            "owner": forms.HiddenInput()
        }


class UserRegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput())


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
