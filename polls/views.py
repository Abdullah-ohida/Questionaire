from collections import defaultdict

from django.shortcuts import render
from .models import Question, Choice


# Create your views here.

def home(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    print(questions[0].choice_set.all())
    return render(request, 'polls/home.html', context)
