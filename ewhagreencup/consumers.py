from channels.generic.websocket import AsyncWebsocketConsumer
import json

class LocationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("location_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("location_group", self.channel_name)

    async def send_location(self, event):
        latitude = event['latitude']
        longitude = event['longitude']
        await self.send(text_data=json.dumps({
            'latitude': latitude,
            'longitude': longitude
        }))

