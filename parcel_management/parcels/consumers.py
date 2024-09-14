# your_app_name/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Parcel

class ParcelConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.tracking_number = self.scope['url_route']['kwargs']['tracking_number']
        self.room_group_name = f'parcel_{self.tracking_number}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def update_status(self, event):
        status = event['status']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'status': status
        }))
