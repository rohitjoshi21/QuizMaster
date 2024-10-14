from django.urls import path
from . import views

urlpatterns = [
    path("",views.studenthomepage,name="student"),
    path("quiz",views.quiz,name="quiz"),
    path("leaderboard",views.leaderboard,name="leaderboard"),
    path("account",views.account,name="account")
]
