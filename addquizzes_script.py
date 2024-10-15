import os
import django
import csv
from django.contrib.auth.hashers import check_password

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "QuizMaster.settings")
django.setup()

# Now you can import your Django models
from users.models import OrganizationUser
from dashboard.models import Quiz, Question

username = "pea"
password = "pea"

orguser = OrganizationUser.objects.get(username=username)
if not check_password(password, orguser.password):
    raise ValueError("Password not matched")

quiztitle = "Quiz Sample"
quizdescription = "Description Here"

quiz = Quiz(title=quiztitle, description=quizdescription, organization=orguser)
quiz.save()

questioncsv = open("questioncollection.csv")
reader = csv.DictReader(questioncsv)

for row in reader:
    questiontext = row['question_text']
    answera = row['answera']
    answerb = row['answerb']
    answerc = row['answerc']
    answerd = row['answerd']
    correctanswer = row['correctanswer']

    question = Question(organization=orguser, question_text=questiontext, answera=answera, answerb=answerb, answerc=answerc, answerd=answerd, correctanswer=correctanswer)
    question.save()
  
  
    quiz.questions.add(question)

print("Quiz and questions have been successfully added to the database.")