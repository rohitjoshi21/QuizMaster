from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage),
    path("login",views.CustomLoginView.as_view(),name="login"),
    path("signup",views.SignupView.as_view())
]
