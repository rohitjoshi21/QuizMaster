import csv
from io import StringIO
from dashboard.models import Quiz, Question

def add(orguser,quiztitle,quizdescription,csvfile):

    if orguser.__class__.__name__ != "OrganizationUser":
        raise PermissionError("This user is not permittted to create quizzes")

    quiz = Quiz(title=quiztitle, description=quizdescription, organization=orguser)
    quiz.save()

    csv_content = csvfile.read().decode('utf-8')
    reader = csv.DictReader(StringIO(csv_content))
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

    return quiz.questions.count()