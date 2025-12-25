from django.urls import path
from . import views

app_name = 'app'  # namespace

urlpatterns = [
    path('', views.main_page, name='main'),               
#    path('new/', views.hot_questions, name='new'),         
    path('hot/', views.hot_questions, name='hot'),            
    path('tag/<str:tag_name>/', views.tag_questions, name='tag'),
    path('question/<int:question_id>/', views.one_question, name='question'),
]
