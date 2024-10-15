from django.db import models

from django.contrib.auth.models import User

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    organization = models.ForeignKey('users.OrganizationUser', on_delete=models.CASCADE, related_name='quizzes',default=1)
    updated_at = models.DateTimeField(auto_now=True)
    questions = models.ManyToManyField('Question',blank=True)

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.title


class Question(models.Model):
    options = (
        ('a','a'),
        ('b','b'),
        ('c','c'),
        ('d','d')
        )
    organization = models.ForeignKey('users.OrganizationUser', on_delete=models.CASCADE, related_name='questions',default=1)
    question_text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    answera = models.CharField(max_length=50)
    answerb = models.CharField(max_length=50)
    answerc = models.CharField(max_length=50)
    answerd = models.CharField(max_length=50)
    correctanswer = models.CharField(max_length=1,choices=options)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.question_text



