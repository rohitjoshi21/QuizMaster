from django import forms
from .models import MyUser


class LoginForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ["username","password"]
        labels = {
            "username":"User Name",
            "password": "Password"
        }

class SignupForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ["first_name","last_name","username","email","password","user_type"]