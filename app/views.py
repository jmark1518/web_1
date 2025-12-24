from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Tag, User, Answer
from django.core.paginator import Paginator
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, SignUpForm, ProfileEditForm, QuestionForm, AnswerForm
from django.urls import reverse

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
    paginator = Paginator(questions, per_page=5)
    page_number = request.GET.get('page')
    question_page = paginator.get_page(page_number)
    return render(request, 'index.html', {'questions': question_page})

def hot_questions(request):
    questions = Question.objects.hot()
    paginator = Paginator(questions, per_page=5)
    page_number = request.GET.get('page')
    question_page = paginator.get_page(page_number)
    return render(request, 'hot.html', {'questions': question_page})

def tag_questions(request, tag_name):
    questions = Question.objects.filter(tags__name=tag_name)
    paginator = Paginator(questions, 2)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'index.html', {'page': page, 'tag_name': tag_name})

def one_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = question.answer.all().order_by('-created_at')
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.save()
            return HttpResponseRedirect(f"{question.get_url()}#answer-{answer.id}")
    else:
        form = AnswerForm()
    
    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
        'form': form
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', '/')
                return redirect(next_url)
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile, user=request.user)
        if form.is_valid():
            user = request.user
            user.email = form.cleaned_data['email']
            user.save()
            form.save()
            messages.success(request, 'Профиль успешно обновлен!')
            return redirect('profile_edit')
    else:
        form = ProfileEditForm(instance=request.user.profile, user=request.user)
    
    return render(request, 'settings.html', {'form': form})

@login_required
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            
            tag_names = form.cleaned_data['tag_names'].split(',')
            for tag_name in tag_names:
                tag_name = tag_name.strip()
                if tag_name:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    question.tags.add(tag)
            
            return redirect(question.get_url())
    else:
        form = QuestionForm()
    
    return render(request, 'ask.html', {'form': form})
