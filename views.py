from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from .models import Question, Tag, User
from django.core.paginator import Paginator


def hello_view(request):
    return HttpResponse("Привет, мир!")

def bye_view(request):
    return HttpResponse("Пока, мир!")

def hello_template_view(request):
    context = {'name': 'Мир'}
    return render(request, 'hello.html', context)


def base(request):
    return render(request, 'base.html')


def main_page(request):
    questions = Question.objects.all().order_by('-created_at')
    paginator=Paginator(questions, per_page=5)
    page_number = request.GET.get('page')
    question_page=paginator.get_page(page_number)


    # Передаём список вопросов в шаблон
    return render(request, 'index.html', {'questions': question_page})

def hot_questions(request):
    questions = Question.objects.hot()
    paginator=Paginator(questions, per_page=5)
    page_number = request.GET.get('page')
    question_page=paginator.get_page(page_number)

    # Передаём список вопросов в шаблон
    return render(request, 'hot.html', {'questions': question_page})


def tag_questions(request, tag_name):
    questions = Question.objects.filter(tags__name=tag_name)
    paginator = Paginator(questions, 2)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'index.html', {'page': page, 'title': 'Тег: {tag_name}'})

def one_question(request, question_id):
    answers = []
    for i in range(1, 3):
        answers.append({
            'title': 'title ' + str(i),
            'id': i,
            'text': 'text ' + str(i),
        })
    question = get_object_or_404(Question, id=question_id)
    # Передаём список вопросов в шаблон
    return render(request, 'question.html', {'question': question, 'answers' : answers})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def create_question(request):
    return render(request, 'ask.html')

def profile(request):
    return render(request, 'settings.html')
