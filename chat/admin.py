from django.contrib import admin
from .models import ChatRoom, ChatHistory

admin.site.register(ChatRoom)
admin.site.register(ChatHistory)