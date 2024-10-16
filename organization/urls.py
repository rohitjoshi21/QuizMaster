from django.urls import path
from . import views

from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.urls import reverse

urlpatterns = [
    path("",views.homepage,name="organization"),
    path("quiz",views.quizzes,name="oquiz"),
    path("quiz/addquiz",views.AddQuizView.as_view(),name='addquiz'),
    path("leaderboard",views.leaderboard,name="oleaderboard"),
    path("account",views.account,name="oaccount"),
    path("account/logout",views.user_logout,name="ologout"),
    path("quiz/<int:quiz_id>",views.submission,name="osubmission")
]

