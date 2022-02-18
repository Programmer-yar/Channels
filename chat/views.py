from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse
from .models import ChatRoom

class CreateJoinChat(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		return render(request, 'chat/index.html')

	def post(self, request, *args, **kwargs):
		room_name = request.POST.get('room_name')
		obj, created = ChatRoom.objects.get_or_create(room_name=room_name)
		obj.participants.add(request.user)
		obj.save()
		return redirect(reverse('room', args={room_name}))

def index(request):
	return render(request, 'chat/index.html')


@login_required
def room(request, room_name):
	return render(request, 'chat/room.html', {'room_name':room_name})
