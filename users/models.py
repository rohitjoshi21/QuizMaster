from django.db import models
from django.contrib.auth.models import User

class OrganizationUser(User):
    user_type = models.CharField(max_length=20,default="organization")
    organizationname = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Organization Admin"
        verbose_name_plural = "Organization Admins"
    # def __str__()

class StudentUser(User):
    user_type = models.CharField(max_length=20,default="student")
    organization = models.ForeignKey(OrganizationUser, on_delete=models.CASCADE,related_name='students',default=1)
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"