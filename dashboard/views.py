from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from users.models import StudentUser
from .models import Quiz, Question
from django.views import View

def check_student(user):
    return StudentUser.objects.get(username=user.username).user_type == "student"

@login_required
@user_passes_test(check_student)
def studenthomepage(request):
    return render(request,"dashboard/dashboard.html",{
        'active':'dashboard'
    })

@login_required
@user_passes_test(check_student)
def quiz(request):
    stduser = StudentUser.objects.get(username = request.user.username)
    quizzes = Quiz.objects.filter(organization=stduser.organization)
    return render(request,"dashboard/quiz.html",{
        'active':'quiz',
        'quizzes':quizzes
    })

class QuizView(View):
    def get(self, request, quiz_id, question_num=1):
        """
        Handles the display of the quiz and its questions, one at a time.
        """
        quiz = get_object_or_404(Quiz, id=quiz_id)
        
        questions = quiz.questions.all()
        
        # Ensure the question number is valid
        if question_num < 1 or question_num > questions.count():
            return redirect('quiz_view', quiz_id=quiz_id, question_num=1)
        
        # Get the specific question based on the question number
        current_question = questions[question_num - 1]
        
        # Check if the quiz is over
        
            
        if question_num > questions.count():
            return redirect('quiz_complete', quiz_id=quiz_id)  # Redirect to completion page
        
        context = {
            'quiz': quiz,
            'question': current_question,
            'question_num': question_num,
            'total_questions': questions.count(),
            'lastquestion': False
        }
        context['lastquestion'] = question_num == questions.count()

        return render(request, 'dashboard/quiz_view.html', context)

    def post(self, request, quiz_id, question_num):
        """
        Handle the "Next" button click and load the next question.
        """
        # Get the quiz object and current question
        quiz = get_object_or_404(Quiz, id=quiz_id)
        questions = quiz.questions.all()

        print(request.POST['selected_option'])

        if question_num < questions.count():
            return redirect('quiz_view', quiz_id=quiz_id, question_num=question_num + 1)
        

        return redirect('quiz_complete', quiz_id=quiz_id)
    
def quiz_complete(request,quiz_id):

    quiz = get_object_or_404(Quiz, id=quiz_id)
    correctanswers = [question.correctanswer for question in quiz.questions.all()]


    return render(request,"dashboard/quiz_submitted.html",{
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
    user = StudentUser.objects.get(username=request.user.username)
    return render(request,"dashboard/account.html",{
        'active':'account',
        'user': user
    })


