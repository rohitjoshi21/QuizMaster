from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test
from users.models import MyUser

def check_student(user):
    return MyUser.objects.get(username=user.username).user_type == "student"

@login_required
@user_passes_test(check_student)
def homepage(request):
    return render(request,"dashboard/homepage.html")
