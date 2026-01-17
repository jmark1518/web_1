from django.urls import path
from . import views

app_name = 'app'  # namespace

urlpatterns = [
    path('', views.main_page, name='main'),               
    path('hot/', views.hot_questions, name='hot'),            
    path('tag/<str:tag_name>/', views.tag_questions, name='tag'),
    path('question/<int:question_id>/', views.one_question, name='question'),
    path('api/like_question/', views.like_question, name='like_question'),
    path('api/mark_correct/', views.mark_correct_answer, name='mark_correct'),
    path('user/<int:user_id>/', views.user_profile, name='user_profile'),
]
