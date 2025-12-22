from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

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
    questions = []
    for i in range(1, 30):
        questions.append({
            'title': 'title ' + str(i),
            'id': i,
            'text': 'text ' + str(i),
        })
    # Передаём список вопросов в шаблон
    return render(request, 'index.html', {'questions': questions})

def hot_questions(request):
    questions = []
    for i in range(1, 30):
        questions.append({
            'title': 'title ' + str(i),
            'id': i,
            'text': 'text ' + str(i),
        })
    # Передаём список вопросов в шаблон
    return render(request, 'hot.html', {'questions': questions})

def tag_questions(request):
    return HttpResponse("cписок вопросов по тэгу")

def one_question(request):
    answers = []
    for i in range(1, 3):
        answers.append({
            'title': 'title ' + str(i),
            'id': i,
            'text': 'text ' + str(i),
        })
    # Передаём список вопросов в шаблон
    return render(request, 'question.html', {'answers': answers})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def create_question(request):
    return render(request, 'ask.html')

def profile(request):
    return render(request, 'settings.html')
