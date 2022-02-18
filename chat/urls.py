from django.urls import path

from . import views

urlpatterns = [
	path('', views.CreateJoinChat.as_view(), name='index'),
	# path('<str:room_name>/', views.CreateJoinChat.as_view(), name='room'),
	path('<str:room_name>/', views.room, name='room'),
	]