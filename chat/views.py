from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse
from .models import ChatRoom

class CreateJoinChat(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		context = {
			'users': User.objects.exclude(username=request.user.username)
			}
		return render(request, 'chat/index.html', context)

	def post(self, request, *args, **kwargs):
		""" get room name and chat reciever
		- if chat room already exists redirects user towards it
		- else creates new chat room and add both users
		"""
		room_name = request.POST.get('room_name')
		chat_with = request.POST.get('users')
		with_user = User.objects.get(id=int(chat_with))
		obj, created = ChatRoom.objects.get_or_create(room_name=room_name)
		if created:
			obj.participants.add(request.user)
			obj.participants.add(with_user)
			obj.save()
		return redirect(reverse('room', args={room_name}))

def index(request):
	return render(request, 'chat/index.html')


@login_required
def room(request, room_name):
	""" gets 'room_name'
	- displays the chat room if user is in participants
	- raise "PermissionDenied" Error if user is not a participant
	"""
	chat_room = ChatRoom.objects.get(room_name=room_name)
	if request.user in chat_room.participants.all():
		return render(request, 'chat/room.html', {'room_name':room_name})
	raise PermissionDenied
