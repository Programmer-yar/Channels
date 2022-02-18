from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ChatRoom

def index(request):
	return render(request, 'chat/index.html')

def get_or_create_chat_room(request):
	pass

@login_required
def room(request, room_name):
	obj, created = ChatRoom.objects.get_or_create(room_name=room_name)
	obj.participants.add(request.user)
	obj.save()
	return render(request, 'chat/room.html', {'room_name':room_name})
