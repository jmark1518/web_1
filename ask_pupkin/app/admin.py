from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Question, Tag, Profile, Answer, QuestionLike, AnswerLike

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar']
    search_fields = ['user__username']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'author', 'created_at']
    filter_horizontal = ['tags']
    search_fields = ['text', 'author__username']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['text', 'question', 'author', 'created_at', 'is_correct']
    search_fields = ['text', 'author__username']

@admin.register(QuestionLike)
class QuestionLikeAdmin(admin.ModelAdmin):
    list_display = ['question', 'user', 'created_at']

@admin.register(AnswerLike)
class AnswerLikeAdmin(admin.ModelAdmin):
    list_display = ['answer', 'user', 'created_at']
