from django.db import models

# Create your models here.
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # 새로운 필드 추가 예시
    # 사용자는 여러 개의 AI를 가질 수 있음 (ManyToMany 관계)
    ainame = models.ManyToManyField('AI', related_name='users', blank=True)

    def __str__(self):
        return self.username
    
class AI(models.Model):
    ainame = models.CharField(max_length=100, unique=True)
    prompt = models.TextField()
    personality = models.CharField(
        max_length=20,
        choices=[
            ('calm', '차분함'),
            ('active', '활발함'),
            ('tsundere', '츤데레'),
            ('playful', '장난꾸러기'),
            ('mysterious', '신비로움'),
            ('intelligent', '지적인')
        ],
        default='calm'
    )

    def __str__(self):
        return self.ainame

#User와 AI의 관계 모델
class UserAI(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ai = models.ForeignKey(AI, on_delete=models.CASCADE)
    affection = models.IntegerField(default=0)  # 호감도 필드 (0~100)

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
