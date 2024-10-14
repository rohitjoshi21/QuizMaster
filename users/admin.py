from django.contrib import admin
from .models import StudentUser, OrganizationUser
# Register your models here.


admin.site.register(OrganizationUser)
admin.site.register(StudentUser)
