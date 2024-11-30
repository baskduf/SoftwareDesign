from django.db import models
from django.utils import timezone
# Create your models here.
    
class AI(models.Model):
    ainame = models.CharField(max_length=100, unique=True)
    prompt = models.TextField()
    
    description = models.TextField(blank=True)
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
    recommend_count = models.PositiveIntegerField(default=0)  # 추천 횟수 필드 추가
    created_at = models.DateTimeField(auto_now_add=True)  # default 제거
    
    def recommend(self):
        self.recommend_count += 1
        self.save()

    def __str__(self):
        return self.ainame
    
    def get_image_url(self):
        return f'/static/img/{self.ainame}.jfif'  # 파일 확장자가 jfif 가정
    
from django.conf import settings
from django.db import models

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Custom user 모델 사용
    ai = models.ForeignKey(AI, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} on {self.ai.ainame}'