from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User # 사용하지 마세요.
# from django.contrib.auth import get_user_model
from django.conf import settings
# settings.AUTH_USER_MODEL   # 윗줄 사용하기
# 위 두줄이 환경변수처럼 사용하기
# default 값이 'auth.User'

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    hit = models.IntegerField(default=0, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'<Board ({self.id})> : {self.title}'
        
    def get_absolute_url(self):
        # 'self.pk/'
        return reverse('boards:detail', args=[self.pk])
        
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'<Comment ({self.id})> : {self.content}'
        

        
    