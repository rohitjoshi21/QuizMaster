from django.db import models
from django.contrib.auth.models import User

class MyUser(User):
    type_choices = {
        "student":"Student",
        "organization":"Organization"
    }
    user_type = models.CharField(max_length=20,choices=type_choices)
    

