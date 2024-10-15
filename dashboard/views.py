from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from users.models import StudentUser
from .models import Quiz, Question, Submission
from django.views import View
from django.contrib.auth import logout
from django.urls import reverse


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
        

        quiz = get_object_or_404(Quiz, id=quiz_id)
        questions = quiz.questions.all()


        answers = request.session.get('answers')
        if answers == None:
            answers = ['' for i in range(questions.count())]
        request.session['answers'] = answers

        
        
        # Ensure the question number is valid
        if question_num < 1 or question_num > questions.count():
            return redirect('quiz_view', quiz_id=quiz_id, question_num=1)
        
        # Get the specific question based on the question number
        current_question = questions[question_num - 1]
        
        # Check if the quiz is over
        
            
        if question_num > questions.count():
            return redirect('quiz_complete', quiz_id=quiz_id)  # Redirect to completion page
        
        context = {
            'active':'quiz',
            'quiz': quiz,
            'question': current_question,
            'question_num': question_num,
            'total_questions': questions.count(),
            'lastquestion': False,
            'question_range':list(range(1,questions.count()+1))
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


        answers = request.session.get('answers')
        answers[question_num-1] = request.POST.get('selected_option')
        request.session['answers'] = answers
  


        if question_num < questions.count():
            return redirect('quiz_view', quiz_id=quiz_id, question_num=question_num + 1)
        

        return redirect('quiz_complete', quiz_id=quiz_id)
    
def quiz_complete(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    actual_answers = [question.correctanswer for question in quiz.questions.all()]
    submitted_answers = request.session.get('answers')
    correctly_answered = [actual_answers[i] == submitted_answers[i] for i in range(len(actual_answers))]
    correct_count = sum(correctly_answered)
    incorrect_count = len(actual_answers) - correct_count

    user = StudentUser.objects.get(username = request.user.username)

    #Saving this submission in database for future analysis
    submission = Submission(user=user,quiz=quiz,correctsubmission=correct_count)
    submission.save()

    # Create a list of tuples containing question text, submitted answer, correct answer, and whether it's correct
    results = []
    for i in range(len(actual_answers)):
        results.append((quiz.questions.all()[i].question_text, submitted_answers[i], actual_answers[i], correctly_answered[i]))

    return render(request, "dashboard/quiz_submitted.html", {
        'quiz':quiz,
        'active': 'quiz',
        'correct_count': correct_count,
        'incorrect_count': incorrect_count,
        'results': results
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


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse("login"))
