from django.contrib import admin
from .models import StudentUser, OrganizationUser
# Register your models here.

class StudentUserAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(organization=request.user)

admin.site.register(OrganizationUser)
admin.site.register(StudentUser, StudentUserAdmin)
