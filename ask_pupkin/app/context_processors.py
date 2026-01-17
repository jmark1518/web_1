from django.db.models import Count
from .models import Tag, User

def popular_tags(request):
    tags = Tag.objects.annotate(num_questions=Count('questions')).order_by('-num_questions')[:10]
    return {'popular_tags': tags}

#def best_members(request):
#    members = User.objects.annotate(num_questions=Count('questions')).order_by('-num_questions')[:5]
#    return {'best_members': members}




def best_members(request):
    # Пользователи с наибольшим количеством вопросов + ответов
    members = User.objects.annotate(
        total_activity=Count('questions') + Count('answers')
    ).order_by('-total_activity')[:10]
    return {'best_members': members}
