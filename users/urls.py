from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("",TemplateView.as_view(template_name="users/homepage.html")),
    path("team",TemplateView.as_view(template_name="users/team.html")),
    path("login",views.CustomLoginView.as_view(),name="login"),
    path("signup",views.SignupView.as_view()),
    path("signup/organization",views.OrgSignUpView.as_view(),name="orgsignup"),
    path("signup/student",views.StdSignUpView.as_view(),name="stdsignup")
]
