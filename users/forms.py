from django import forms
from .models import StudentUser, OrganizationUser


class LoginForm(forms.ModelForm):
    class Meta:
        model = StudentUser
        fields = ["username","password"]
        labels = {
            "username":"User Name",
            "password": "Password"
        }

class StudentSignupForm(forms.ModelForm):
    class Meta:
        model = StudentUser
        fields = ["first_name","last_name","username","email","password", "organization"]


class OrganizationSignupForm(forms.ModelForm):
    class Meta:
        model = OrganizationUser
        fields = ["organizationname","username","email","password"]