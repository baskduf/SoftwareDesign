from django.db import models

# Create your models here.
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from aiservice.models import AI

class User(AbstractUser):
    # 새로운 필드 추가 예시
    # 사용자는 여러 개의 AI를 가질 수 있음 (ManyToMany 관계)
    ainame = models.ManyToManyField('aiservice.AI', related_name='users', blank=True)

    def __str__(self):
        return self.username
    
    def subscribed_ais(self):
        return [user_ai.ai for user_ai in UserAI.objects.filter(user=self, subscribed=True)]

#User와 AI의 관계 모델
class UserAI(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ai = models.ForeignKey(AI, on_delete=models.CASCADE)
    affection = models.IntegerField(default=0)  # 호감도 필드 (0~100)
    subscribed = models.BooleanField(default=False)  # AI 구독 상태

    def subscribe(self):
        self.subscribed = True
        self.save()

    def unsubscribe(self):
        self.subscribed = False
        self.save()

    class Meta:
        unique_together = ('user', 'ai')

    def __str__(self):
        return f"{self.user.username} - {self.ai.ainame} (Affection: {self.affection})"
    
class ChatLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_logs')
    ai = models.ForeignKey(AI, on_delete=models.CASCADE, related_name='chat_logs')

    message = models.TextField()  # 개별 채팅 메시지
    timestamp = models.DateTimeField(auto_now_add=True)  # 채팅 시간 기록

    def __str__(self):
        return f'Chat between {self.user.username} and {self.ai.ainame} at {self.timestamp}'
