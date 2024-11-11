from django.db import models

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
    
    def recommend(self):
        self.recommend_count += 1
        self.save()

    def __str__(self):
        return self.ainame
    
    def get_image_url(self):
        return f'/static/img/{self.ainame}.jfif'  # 파일 확장자가 jfif 가정