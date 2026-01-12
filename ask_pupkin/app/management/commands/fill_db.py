import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import *

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int)

    def handle(self, *args, **options):
        ratio = int(options['ratio'])
        
        QuestionLike.objects.all().delete()
        AnswerLike.objects.all().delete()
        Answer.objects.all().delete()
        Question.objects.all().delete()
        Tag.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()
        
        users = []
        for i in range(ratio):
            user = User.objects.create_user(username=f'user{i}', email=f'user{i}@mail.ru')
#            Profile.objects.create(user=user)
            users.append(user)
        self.stdout.write(f'Users: {ratio}')
        
        tags = []
        tag_base = ['python', 'django', 'cpp', 'linux', 'js', 'sql', 'html', 'css']
        for i in range(ratio):
            name = f"{random.choice(tag_base)}{i}"
            tag = Tag.objects.create(name=name)
            tags.append(tag)
        self.stdout.write(f'Tags: {ratio}')
        
        questions = []
        for i in range(ratio * 10):
            q = Question.objects.create(
                author=random.choice(users),
                title=f'Как изучить {random.choice(tag_base)}? Вопрос {i}',
                text=f'Вопрос {i}: как изучить {random.choice(tags).name}?'
            )
            q.tags.set(random.sample(tags, k=random.randint(1, 3)))
            questions.append(q)
        self.stdout.write(f'Questions: {ratio*10}')
        
        for i in range(ratio * 100):
            Answer.objects.create(
                question=random.choice(questions),
                author=random.choice(users),
                text=f'Ответ {i}: используйте документацию!'
            )
        self.stdout.write(f'Answers: {ratio*100}')
        
        created_likes = 0
        for _ in range(ratio * 200):
            question = random.choice(questions)
            user = random.choice(users)
            if not QuestionLike.objects.filter(question=question, user=user).exists():
                is_like = random.choice([True, False]) 
                QuestionLike.objects.create(question=question, user=user)
                created_likes += 1
        
        self.stdout.write(self.style.SUCCESS(f'Likes: {created_likes}'))
        self.stdout.write(self.style.SUCCESS(f'Готово! ratio={ratio}'))

