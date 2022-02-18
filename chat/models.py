from django.contrib.auth.models import User
from django.db import models

class ChatRoom(models.Model):
    participants = models.ManyToManyField(User, related_name='chat_rooms')
    room_name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.room_name

class ChatHistory(models.Model):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.SET_NULL,
        related_name='chats', null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
        related_name='chats')
    message = models.TextField()
    
