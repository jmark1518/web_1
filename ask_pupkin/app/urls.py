from django.urls import path
from . import views

app_name = 'app'  # namespace

urlpatterns = [
    # ДЗ3 — ТОЛЬКО эти 4 страницы!
    path('', views.main_page, name='main'),                    # /
    path('new/', views.hot_questions, name='new'),             # /new/
    path('hot/', views.hot_questions, name='hot'),             # /hot/
    path('tag/<str:tag_name>/', views.tag_questions, name='tag'),  # /tag/python0/
    path('question/<int:question_id>/', views.one_question, name='question'),  # /question/123/
]
