from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test
from users.models import StudentUser as MyUser

def check_student(user):
    return MyUser.objects.get(username=user.username).user_type == "student"

@login_required
@user_passes_test(check_student)
def studenthomepage(request):
    return render(request,"dashboard/dashboard.html",{
        'active':'dashboard'
    })

@login_required
@user_passes_test(check_student)
def quiz(request):
    return render(request,"dashboard/quiz.html",{
        'active':'quiz'
    })

@login_required
@user_passes_test(check_student)
def leaderboard(request):
    return render(request,"dashboard/leaderboard.html",{
        'active':'leaderboard'
    })

@login_required
@user_passes_test(check_student)
def account(request):
    user = MyUser.objects.get(username=request.user.username)
    return render(request,"dashboard/account.html",{
        'active':'account',
        'user': user
    })


