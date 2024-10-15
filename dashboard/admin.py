from django.contrib import admin

from .models import Quiz, Question, Submission
from users.models import OrganizationUser

class QuizAdmin(admin.ModelAdmin):
    # fields = ('title','description')

    exclude = ('organization',)

    def save_model(self, request, obj, form, change):
        """
        Automatically assign the organization to the Quiz based on the logged-in user's organization.
        """
        if not request.user.is_superuser:  # Check if the user is not a superuser
            obj.organization = OrganizationUser.objects.get(username=request.user.username)  # Set organization to the logged-in user's organization
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(organization=request.user)
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "questions":
            kwargs["queryset"] = Question.objects.filter(organization=request.user)
        return super().formfield_for_manytomany(db_field, request, **kwargs)
    
class QuestionAdmin(admin.ModelAdmin):

    exclude = ('organization',)

    def save_model(self, request, obj, form, change):
        """
        Automatically assign the organization to the Quiz based on the logged-in user's organization.
        """
        if not request.user.is_superuser:  # Check if the user is not a superuser
            obj.organization = OrganizationUser.objects.get(username=request.user.username)  # Set organization to the logged-in user's organization
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(organization=request.user)

# class SubmissionAdmin(models.Admin):
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             return qs
         
#         return qs.filter(quiz__in=request.user)

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Submission)