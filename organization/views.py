from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from users.models import StudentUser, OrganizationUser
from dashboard.models import Quiz, Submission
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import logout
from django.urls import reverse
from .forms import NewQuizForm
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin


def check_organization(user):
    return OrganizationUser.objects.get(username=user.username).user_type == "organization"

def homepage(request):
    org = OrganizationUser.objects.get(username = request.user.username)
    user_count = StudentUser.objects.filter(organization=org).count()
    quiz_count = Quiz.objects.filter(organization=org).count()
    submission_count = Submission.objects.filter(quiz__organization=org).count()

    context = {
        'user_count': user_count,
        'quiz_count': quiz_count,
        'submission_count': submission_count,
    }
    return render(request, 'organization/homepage.html', context)

def leaderboard(request):
    pass

@login_required
@user_passes_test(check_organization)
def quizzes(request):
    org = OrganizationUser.objects.get(username = request.user.username)
    quizzes = Quiz.objects.filter(organization=org)
    return render(request,"organization/quizzes.html",{
        'active':'quiz',
        'quizzes':quizzes
    })

class AddQuizView(LoginRequiredMixin,FormView):
    template_name = "organization/addquiz.html"
    form_class = NewQuizForm
    success_url = "/organization/quiz"

    def form_valid(self, form):
        org = OrganizationUser.objects.get(username = self.request.user.username)
        data = form.cleaned_data

        from . import quizadder

        quiztitle = data['title']
        quizdescription = data['description']
        csvfile = self.request.FILES['csvfile']

        quizadder.add(org,quiztitle,quizdescription,csvfile)

        return super().form_valid(form)

    


@user_passes_test(check_organization)
def account(request):
    user = OrganizationUser.objects.get(username=request.user.username)
    return render(request,"organization/account.html",{
        'active':'account',
        'user': user
    })


@login_required
def user_logout(request):
    logout(request)
    return redirect("login")


@login_required
@user_passes_test(check_organization)
def submission(request,quiz_id):

    quiz = Quiz.objects.get(id=quiz_id)
    valid_submissions = Submission.objects.filter(quiz=quiz).order_by("-timestamp")
    
    percentages = []
    for submission in valid_submissions:
        correct_score = submission.correctsubmission
        total_questions = submission.quiz.questions.count()
        percentage = correct_score / total_questions * 100
        percentages.append(percentage)


    return render(request, 'organization/submissions.html', {
        'sub_per':zip(valid_submissions,percentages),
        'valid_submissions': valid_submissions,
        'percentages': percentages,
        'quiztitle':quiz.title
    })