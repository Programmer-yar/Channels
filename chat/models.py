from django.db import models

class ChatRoom(models.Model):
    participants = models.ManyToManyField(User, related_name='chat_rooms')
    room_name = models.CharField(max_lenght=200)
    def __str__(self):
        return self.room_name

class ChatHistory(models.Model):
    chat_room = models.ForeginKey(ChatRoom, on_delete=models.SET_NULL,
        related_name='chats', null=True)
    owner = models.ForeginKey(User, on_delete=models.CASCADE,
        related_name='chats')
    message = models.TextField()
