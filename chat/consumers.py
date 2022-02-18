""" Views for asgi applications like channels """
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer #WebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """- self.scope
        -> just like 'request' object
        -> contains a lot of information including room_name,
            user data, authentication data
        -> in channels, middlewares add data to 'self.scope' the same way
            middlewares add data to 'request' object in django
        """
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}' #'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
            )

        # if not called the connection will be rejected and closed
        if self.scope['user'].is_authenticated:
            await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # print(message, self.room_name, self.room_group_name)
        # print(self.scope['user'].is_authenticated)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
            }))