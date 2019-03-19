from django.db import models
from django.urls import reverse

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    hit = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'<Board ({self.id})> : {self.title}'
        
    def get_absolute_url(self):
        # 'self.pk/'
        return reverse('boards:detail', args=[self.pk])