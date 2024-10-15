from django.urls import path
from . import views

urlpatterns = [
    path("",views.studenthomepage,name="student"),
    path("quiz",views.quiz,name="quiz"),
    path('quiz/<int:quiz_id>/question/<int:question_num>/', views.QuizView.as_view(), name='quiz_view'),
    path('quiz/<int:quiz_id>/complete/', views.quiz_complete, name='quiz_complete'),
    path("leaderboard",views.leaderboard,name="leaderboard"),
    path("account",views.account,name="account")
]
