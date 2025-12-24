from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count, Q


from django.db.models.signals import post_save
from django.dispatch import receiver



class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    
    def __str__(self):
        return f"Profile {self.user.username}"

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-created_at')
    
    def hot(self):
        return self.annotate(
            likes_count=Count('questionlike', distinct=True),
            answers_count=Count('answer', distinct=True)
        ).order_by('-likes_count', '-created_at')

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='questions', blank=True)
    
    objects = QuestionManager()
    
    def get_url(self):
        return f"/question/{self.id}/"
    
    def __str__(self):
        return self.text[:50]

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text[:50]

class QuestionLike(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='questionlike')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('question', 'user')

class AnswerLike(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='answerlike')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('answer', 'user')





@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
