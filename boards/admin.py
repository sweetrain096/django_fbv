from django.contrib import admin
from .models import Board, Comment
# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'hit', 'created_at', 'updated_at']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'created_at', 'updated_at', 'user', 'board']

admin.site.register(Board)
admin.site.register(Comment)