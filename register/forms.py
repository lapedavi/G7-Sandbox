from django import forms
from django.contrib.auth.forms import UserCreationForm
from CollectAll.models import SiteUser


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = SiteUser
        fields = ["username", "email", "password1", "password2"]
